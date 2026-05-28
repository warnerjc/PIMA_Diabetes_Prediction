# PIMA Diabetes Prediction

This project builds and deploys a machine learning pipeline for predicting diabetes from the Pima Indians Diabetes dataset.

It includes:
- a notebook-driven workflow for data preparation, model training, and deployment
- Hugging Face integration for dataset/model storage and deployment
- a Streamlit app containerized with Docker
- a sample GitHub Actions workflow for dataset registration, model training, and hosting

Key files:
- `Intro_to_MLOps_w_Github_Actions.ipynb` — project walkthrough and implementation
- `pima.csv` — source dataset
- `self_paced_courses_1_mlops/` — model, deployment, and workflow scripts

Required management steps:
- set `HF_USER` for Hugging Face operations
- set `HF_TOKEN` for Hugging Face operations
- run the notebook or supporting scripts to prepare data, train the model, and deploy
- use `.github/workflows/` to manage automated pipeline execution
