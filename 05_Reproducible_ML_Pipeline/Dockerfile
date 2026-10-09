FROM python:3.13-slim
ENV PYTHONHASHSEED=0
WORKDIR /app
COPY 05_Reproducible_ML_Pipeline/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY 05_Reproducible_ML_Pipeline /app/05_Reproducible_ML_Pipeline
CMD ["python", "/app/05_Reproducible_ML_Pipeline/src/train.py", "--seed", "42"]
