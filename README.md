# Iris DVC Tutorial

> **Machine Learning model versioning with DVC (Data Version Control)**

A hands-on tutorial demonstrating data and model versioning using DVC with the classic Iris dataset. Train two classification models (Logistic Regression and Random Forest) with different dataset sizes and track everything with Git and DVC.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![DVC](https://img.shields.io/badge/DVC-3.30.0-orange.svg)](https://dvc.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-green.svg)](https://scikit-learn.org/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Versions](#versions)
- [DVC Commands Reference](#dvc-commands-reference)
- [Collaboration](#collaboration)
- [What You'll Learn](#what-youll-learn)
- [Requirements](#requirements)
- [License](#license)

---

## 🎯 Overview

This project demonstrates how to use **DVC (Data Version Control)** to version control:
- 📊 **Datasets** - Track different versions of your data
- 🤖 **Models** - Version your trained models
- 📈 **Metrics** - Compare performance across versions
- 🔄 **Experiments** - Easily switch between versions

We train two classifiers on the Iris dataset:
1. **Logistic Regression**
2. **Random Forest**

We create two versions:
- **v1.0**: Trained with 150 samples
- **v2.0**: Trained with 300 samples (augmented data)

---

## ✨ Features

- ✅ **Data versioning** with DVC
- ✅ **Model versioning** with DVC
- ✅ **Two ML algorithms** for comparison
- ✅ **Reproducible pipelines** with `dvc repro`
- ✅ **Remote storage** support (S3, GDrive, Azure)
- ✅ **Team collaboration** workflows
- ✅ **Metrics tracking** across versions
- ✅ **Complete documentation**

---

## 📁 Project Structure

```
iris-dvc-tutorial/
├── .dvc/                   # DVC configuration and cache
│   ├── config              # Remote storage configuration
│   └── cache/              # Local cache (all versions stored here)
│
├── data/
│   ├── iris.csv            # Current dataset (tracked by DVC)
│   └── iris.csv.dvc        # Dataset pointer (tracked by Git)
│
├── models/
│   ├── logistic_regression.pkl     # LR model (tracked by DVC)
│   ├── logistic_regression.pkl.dvc # Model pointer (tracked by Git)
│   ├── random_forest.pkl           # RF model (tracked by DVC)
│   └── random_forest.pkl.dvc       # Model pointer (tracked by Git)
│
├── predictions/
│   ├── lr_predictions.csv          # LR predictions (tracked by DVC)
│   ├── lr_predictions.csv.dvc      # Pointer (tracked by Git)
│   ├── rf_predictions.csv          # RF predictions (tracked by DVC)
│   └── rf_predictions.csv.dvc      # Pointer (tracked by Git)
│
├── train.py                # Training script
├── prepare_data_v1.py      # Create 150-sample dataset
├── prepare_data_v2.py      # Create 300-sample dataset
├── requirements.txt        # Python dependencies
├── metrics.json            # Model performance metrics (tracked by Git)
├── dvc.yaml               # DVC pipeline definition (optional)
├── dvc.lock               # DVC pipeline lock file (optional)
└── README.md              # This file
```

**Key Concept:**
- 🔵 **Git tracks**: Code, `.dvc` files, small files like `metrics.json`
- 🟢 **DVC tracks**: Large files like datasets, models, predictions

---

## 🚀
