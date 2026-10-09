"""Leakage-free, seed-controlled evaluation for Deliverable 05.
Run: PYTHONHASHSEED=0 python src/train.py --seed 42
"""
import argparse, hashlib, json, random
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import make_scorer, precision_score, recall_score, f1_score

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)

def evaluate(seed=42, data_path=None):
    set_seed(seed)
    if data_path is None:
        data_path = Path(__file__).resolve().parents[1] / "data" / "breast_cancer.csv"
    data_path = Path(data_path)
    df = pd.read_csv(data_path)
    X, y = df.drop(columns="target"), df["target"]
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=5000, solver="liblinear", random_state=seed)),
    ])
    scoring = {
        "accuracy":"accuracy",
        "balanced_accuracy":"balanced_accuracy",
        "precision":make_scorer(precision_score, pos_label=1, zero_division=0),
        "recall":make_scorer(recall_score, pos_label=1, zero_division=0),
        "f1":make_scorer(f1_score, pos_label=1, zero_division=0),
        "roc_auc":"roc_auc",
    }
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    raw = cross_validate(pipe, X, y, cv=cv, scoring=scoring, n_jobs=1, return_train_score=False)
    summary = {"seed":seed, "data_md5":hashlib.md5(data_path.read_bytes()).hexdigest()}
    folds = []
    for fold in range(5):
        row={"seed":seed,"fold":fold+1}
        for metric in scoring:
            vals=raw[f"test_{metric}"]
            row[metric]=float(vals[fold])
            summary[f"{metric}_mean"]=float(vals.mean())
            summary[f"{metric}_sd"]=float(vals.std(ddof=1))
        folds.append(row)
    return summary, pd.DataFrame(folds)

if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--seed",type=int,default=42)
    args=ap.parse_args()
    summary,_=evaluate(args.seed)
    print(json.dumps({k:(round(v,5) if isinstance(v,float) else v) for k,v in summary.items()},sort_keys=True))
