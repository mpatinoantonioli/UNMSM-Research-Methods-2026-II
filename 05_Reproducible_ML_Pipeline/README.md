# Deliverable 05 — Reproducible ML Pipeline

**Student:** Miguel Ángel Patiño Antonioli  
**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies — UNMSM  

## Objective
Demonstrate a leakage-free, versioned and auditable ML experiment. The public Wisconsin Diagnostic Breast Cancer dataset is used because it is the Session 5 workshop dataset; `target=1` denotes malignant disease.

## Reproducibility stack
- **Code:** Git / GitHub
- **Data:** DVC + persistent remote
- **Experiments:** MLflow 3.x with SQLite
- **Environment:** pinned direct dependencies + Dockerfile
- **Reporting:** seven seeds, mean ± SD, figures and exact expected output

## Reproduce
```bash
git clone https://github.com/mpatinoantonioli/UNMSM-Research-Methods-2026-II.git
cd UNMSM-Research-Methods-2026-II
dvc pull
pip install -r 05_Reproducible_ML_Pipeline/requirements.txt
PYTHONHASHSEED=0 python 05_Reproducible_ML_Pipeline/src/train.py --seed 42
```

## Expected seed-42 result
- accuracy_mean = 0.97542
- accuracy_sd = 0.01567
- f1_mean = 0.96600
- recall_mean = 0.94828
- roc_auc_mean = 0.99538
- data_md5 = `7d389a2808d8bcf9c30b5933557cdbad`

## Seven-seed headline result
Accuracy = **0.97842 ± 0.00195** across seed-level 5-fold means.  
See `results/seed_summary.csv` and `figures/` for the full audit trail.

## Repeatability check
Run the seed-42 command twice. The JSON line must be identical. The notebook also asserts equality of every fold-level metric.

## Docker
After `dvc pull`:
```bash
docker build -f 05_Reproducible_ML_Pipeline/Dockerfile -t unmsm-d5-repro .
docker run --rm unmsm-d5-repro
```

## Data source
Wisconsin Diagnostic Breast Cancer dataset, UCI Machine Learning Repository (CC BY 4.0).
