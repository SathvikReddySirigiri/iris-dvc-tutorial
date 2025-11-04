# Create README.md
@"
# Iris DVC Tutorial

Machine Learning project demonstrating DVC (Data Version Control) with:
- Iris dataset
- Logistic Regression & Random Forest models
- Data and model versioning

## Setup

\`\`\`bash
# Clone the repo
git clone https://github.com/SathvikReddySirigiri/iris-dvc-tutorial.git
cd iris-dvc-tutorial

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull DVC files
dvc pull
\`\`\`

## Usage

\`\`\`bash
# Train models
python train.py

# Reproduce pipeline
dvc repro
\`\`\`

## Versions

- v1.0: Models trained on 150 samples
- v2.0: Models trained on 300 samples
"@ | Out-File -FilePath README.md -Encoding UTF8

# Add and push
git add README.md
git commit -m "Add README"
git push
