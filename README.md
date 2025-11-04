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

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Git
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/iris-dvc-tutorial.git
cd iris-dvc-tutorial
```

**2. Create and activate virtual environment**

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Pull data and models from DVC remote**

```bash
dvc pull
```

That's it! You're ready to go. 🎉

---

## 💻 Usage

### Training Models

#### Option 1: Train from scratch

```bash
# Create the initial dataset (150 samples)
python prepare_data_v1.py

# Train models
python train.py

# Check results
cat metrics.json  # Linux/macOS
type metrics.json  # Windows
```

#### Option 2: Use DVC pipeline

```bash
# Run the entire pipeline
dvc repro

# This will:
# 1. Check if dependencies changed
# 2. Retrain models if needed
# 3. Update metrics
```

### Viewing Results

**Check metrics:**
```bash
# View current metrics
cat metrics.json

# Compare metrics between versions
dvc metrics diff v1.0 v2.0

# Show metrics for specific version
dvc metrics show v1.0
```

**Check predictions:**
```bash
# View Logistic Regression predictions
head predictions/lr_predictions.csv

# View Random Forest predictions
head predictions/rf_predictions.csv
```

---

## 🔄 Versions

This project has two versions demonstrating dataset and model evolution:

### Version 1.0 (150 samples)

```bash
git checkout v1.0
dvc checkout
```

**What you get:**
- 📊 Dataset: 150 samples (50 per class)
- 🤖 Models: Trained on 150 samples
- 📈 Metrics: ~95% accuracy

**Verify:**
```bash
# Check dataset size (Windows PowerShell)
(Get-Content data/iris.csv | Measure-Object -Line).Lines
# Output: 151 (150 rows + 1 header)

# Check dataset size (Linux/macOS)
wc -l data/iris.csv
# Output: 151

# View metrics
cat metrics.json
```

### Version 2.0 (300 samples)

```bash
git checkout v2.0
dvc checkout
```

**What you get:**
- 📊 Dataset: 300 samples (100 per class, includes augmented data)
- 🤖 Models: Retrained on 300 samples
- 📈 Metrics: ~97% accuracy (improved!)

**Verify:**
```bash
# Check dataset size (Windows PowerShell)
(Get-Content data/iris.csv | Measure-Object -Line).Lines
# Output: 301 (300 rows + 1 header)

# Check dataset size (Linux/macOS)
wc -l data/iris.csv
# Output: 301

# View metrics
cat metrics.json
```

### Comparing Versions

```bash
# Compare metrics
dvc metrics diff v1.0 v2.0

# See what changed in Git
git diff v1.0 v2.0

# See what changed in DVC
dvc diff v1.0 v2.0
```

---

## 📖 Step-by-Step Tutorial

### Creating Version 1.0 from Scratch

```bash
# 1. Initialize project
mkdir iris-dvc-tutorial
cd iris-dvc-tutorial
git init
dvc init
git commit -m "Initialize DVC"

# 2. Create directories
mkdir data models predictions

# 3. Create dataset (150 samples)
python prepare_data_v1.py

# 4. Track dataset with DVC
dvc add data/iris.csv
git add data/iris.csv.dvc data/.gitignore
git commit -m "Add dataset v1 (150 samples)"

# 5. Train models
python train.py

# 6. Track models and predictions
dvc add models/logistic_regression.pkl
dvc add models/random_forest.pkl
dvc add predictions/lr_predictions.csv
dvc add predictions/rf_predictions.csv

# 7. Commit everything
git add models/*.dvc predictions/*.dvc metrics.json .gitignore
git commit -m "First model, trained with 150 samples"
git tag -a "v1.0" -m "model v1.0, 150 samples"
```

### Creating Version 2.0

```bash
# 1. Create augmented dataset (300 samples)
python prepare_data_v2.py

# 2. Update dataset tracking
dvc add data/iris.csv
git add data/iris.csv.dvc
git commit -m "Update dataset to 300 samples"

# 3. Retrain models
python train.py

# 4. Update model tracking
dvc add models/logistic_regression.pkl
dvc add models/random_forest.pkl
dvc add predictions/lr_predictions.csv
dvc add predictions/rf_predictions.csv

# 5. Commit everything
git add models/*.dvc predictions/*.dvc metrics.json
git commit -m "Second model, trained with 300 samples"
git tag -a "v2.0" -m "model v2.0, 300 samples"
```

---

## 📚 DVC Commands Reference

### Basic Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `dvc init` | Initialize DVC in repository | `dvc init` |
| `dvc add <file>` | Track file with DVC | `dvc add data/iris.csv` |
| `dvc checkout` | Restore files to match current Git commit | `dvc checkout` |
| `dvc push` | Upload tracked files to remote storage | `dvc push` |
| `dvc pull` | Download tracked files from remote | `dvc pull` |
| `dvc status` | Show changes in tracked files | `dvc status` |

### Pipeline Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `dvc stage add` | Add a pipeline stage | `dvc stage add -n train -d train.py -o models/*.pkl python train.py` |
| `dvc repro` | Reproduce pipeline (run changed stages) | `dvc repro` |
| `dvc dag` | Show pipeline visualization | `dvc dag` |
| `dvc metrics show` | Display metrics | `dvc metrics show` |
| `dvc metrics diff` | Compare metrics between versions | `dvc metrics diff v1.0 v2.0` |

### Remote Storage Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `dvc remote add` | Add remote storage | `dvc remote add -d myremote s3://bucket/path` |
| `dvc remote list` | List configured remotes | `dvc remote list` |
| `dvc remote modify` | Modify remote configuration | `dvc remote modify myremote region us-west-2` |

---

## 🤝 Collaboration

### For the Project Owner

**1. Set up remote storage**

```bash
# Example: Local remote for testing
mkdir /path/to/dvc-storage
dvc remote add -d myremote /path/to/dvc-storage

# Or use cloud storage
# dvc remote add -d myremote s3://my-bucket/dvc-storage
# dvc remote add -d myremote gdrive://folder-id
```

**2. Push data and models**

```bash
dvc push
git add .dvc/config
git commit -m "Configure DVC remote"
git push
```

### For Team Members

**1. Clone the repository**

```bash
git clone https://github.com/SathvikReddySirigiri/iris-dvc-tutorial.git
cd iris-dvc-tutorial
```

**2. Set up environment**

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Linux/macOS)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**3. Pull data and models**

```bash
dvc pull
```

**4. Verify everything works**

```bash
# Check files exist
ls data/iris.csv
ls models/

# Run training
python train.py

# Or reproduce pipeline
dvc repro
```

### Sharing Updates

**When you make changes:**

```bash
# Make your changes
python prepare_new_data.py

# Track with DVC
dvc add data/iris.csv

# Retrain if needed
dvc repro

# Push to remotes
git add data/iris.csv.dvc dvc.lock metrics.json
git commit -m "Updated dataset and models"
git push
dvc push
```

**Teammates pull updates:**

```bash
git pull
dvc pull
```

---

## 🎓 What You'll Learn

By following this tutorial, you'll learn:

- ✅ How to version control datasets with DVC
- ✅ How to version control ML models
- ✅ How to track metrics across experiments
- ✅ How to switch between different versions
- ✅ How to create reproducible ML pipelines
- ✅ How to collaborate with team members
- ✅ How to set up remote storage for data and models
- ✅ Best practices for ML project organization

---

## 📦 Requirements

```txt
pandas==1.5.3
numpy==1.24.3
scikit-learn==1.3.0
dvc==3.30.0
```

**Optional (for cloud storage):**
```bash
pip install dvc[s3]      # For Amazon S3
pip install dvc[gdrive]  # For Google Drive
pip install dvc[azure]   # For Azure Blob Storage
```

---

## 🛠️ Troubleshooting

### Issue: DVC commands not found

**Solution:**
```bash
# Make sure virtual environment is activated
# You should see (.venv) in your terminal prompt

# Reinstall DVC
pip install dvc
```

### Issue: "Cannot import name 'umask'" on Windows

**Solution:**
```bash
# Reinstall DVC with all dependencies
pip uninstall dvc -y
pip install "dvc[all]"
```

### Issue: Git shows modified .dvc files but data hasn't changed

**Solution:**
```bash
# Checkout the .dvc files from Git
git checkout -- *.dvc

# Then run DVC checkout
dvc checkout
```

### Issue: dvc pull fails

**Solution:**
```bash
# Check if remote is configured
dvc remote list

# Check remote connectivity
dvc remote list --config

# Try pushing first if you're the project owner
dvc push
```

---

## 🔗 Useful Links

- [DVC Documentation](https://dvc.org/doc)
- [DVC Tutorial](https://dvc.org/doc/start)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

