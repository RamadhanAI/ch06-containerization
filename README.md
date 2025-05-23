# Chapter 6: Containerization and Reproducibility

This chapter demonstrates how to package, track, and deploy machine learning workflows with Docker and MLflow — ensuring full reproducibility and portability across environments.

## 🚀 Project Overview

**Goal:** Build a containerized pipeline that tracks ML experiments, models, and metrics using MLflow, all isolated within a Docker environment.

## 🧠 What You’ll Learn

- Docker basics for ML reproducibility
- MLflow for experiment tracking and model registry
- Best practices for containerizing training and inference
- How to avoid the dreaded "it worked on my machine" trap

## 🧰 Tech Stack

- Python 3.9
- Docker
- MLflow
- Scikit-learn
- Pandas, NumPy

## 📁 Folder Structure

ch06-containerization/
├── config/
│ └── config.yaml # Centralized hyperparameters & paths
├── data/
│ └── README.md # Download instructions for training data
├── deployment/
│ └── Dockerfile # Production container
├── mlruns/ # Local MLflow tracking logs
├── scripts/
│ ├── train.py # ML training with MLflow logging
│ └── validate.py # Quick performance check
├── requirements.txt
├── README.md


## 📦 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/RamadhanAI/ch06-containerization.git
cd ch06-containerization
Download or place your training data inside:
data/your_dataset.csv
Install dependencies (optional for local runs):
pip install -r requirements.txt
Run the training script with MLflow:
python scripts/train.py --config config/config.yaml
🐳 Docker Build & Run

Build the container:
docker build -t ch06-mlflow-docker .
Run the training job inside Docker:
docker run -v $(pwd):/app ch06-mlflow-docker
Launch MLflow UI:
mlflow ui
# Visit http://127.0.0.1:5000
✅ GitHub Actions (CI)

This repo includes a CI pipeline to:

Validate Docker builds
Check training script execution
Log MLflow metrics
See .github/workflows/validate.yml.

📘 Related Chapter

This repo is part of Chapter 6: Containerization and Reproducibility of the book:

Applied AI and MLOps: From Idea to Deployment

