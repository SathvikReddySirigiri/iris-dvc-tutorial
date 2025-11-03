"""
Training script for Iris classification using Logistic Regression and Random Forest
Outputs: models, predictions, and metrics
"""
import pandas as pd
import numpy as np
import pickle
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import os

# Set random seed for reproducibility
np.random.seed(42)

def load_data(data_path='data/iris.csv'):
    """Load the iris dataset"""
    df = pd.read_csv(data_path)
    return df

def prepare_features(df):
    """Prepare features and target"""
    X = df.drop('species', axis=1)
    y = df['species']
    return X, y

def train_logistic_regression(X_train, y_train):
    """Train Logistic Regression model"""
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train, y_train):
    """Train Random Forest model"""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test, model_name):
    """Evaluate model and return metrics"""
    y_pred = model.predict(X_test)
    
    metrics = {
        'model': model_name,
        'accuracy': float(accuracy_score(y_test, y_pred)),
        'precision': float(precision_score(y_test, y_pred, average='weighted')),
        'recall': float(recall_score(y_test, y_pred, average='weighted')),
        'f1_score': float(f1_score(y_test, y_pred, average='weighted'))
    }
    
    return metrics, y_pred

def save_model(model, filepath):
    """Save model to pickle file"""
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {filepath}")

def save_predictions(y_test, y_pred, model_name, filepath):
    """Save predictions to CSV"""
    pred_df = pd.DataFrame({
        'actual': y_test.values,
        'predicted': y_pred,
        'model': model_name
    })
    pred_df.to_csv(filepath, index=False)
    print(f"Predictions saved to {filepath}")

def save_metrics(metrics_list, filepath='metrics.json'):
    """Save metrics to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(metrics_list, f, indent=4)
    print(f"Metrics saved to {filepath}")

def main():
    # Create output directories if they don't exist
    os.makedirs('models', exist_ok=True)
    os.makedirs('predictions', exist_ok=True)
    
    # Load data
    print("Loading data...")
    df = load_data()
    print(f"Dataset shape: {df.shape}")
    print(f"Classes: {df['species'].unique()}")
    
    # Prepare features
    X, y = prepare_features(df)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Training set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")
    
    # Train Logistic Regression
    print("\nTraining Logistic Regression...")
    lr_model = train_logistic_regression(X_train, y_train)
    lr_metrics, lr_pred = evaluate_model(lr_model, X_test, y_test, 'Logistic Regression')
    print(f"Logistic Regression Accuracy: {lr_metrics['accuracy']:.4f}")
    
    # Save LR model and predictions
    save_model(lr_model, 'models/logistic_regression.pkl')
    save_predictions(y_test, lr_pred, 'Logistic Regression', 'predictions/lr_predictions.csv')
    
    # Train Random Forest
    print("\nTraining Random Forest...")
    rf_model = train_random_forest(X_train, y_train)
    rf_metrics, rf_pred = evaluate_model(rf_model, X_test, y_test, 'Random Forest')
    print(f"Random Forest Accuracy: {rf_metrics['accuracy']:.4f}")
    
    # Save RF model and predictions
    save_model(rf_model, 'models/random_forest.pkl')
    save_predictions(y_test, rf_pred, 'Random Forest', 'predictions/rf_predictions.csv')
    
    # Save all metrics
    metrics_list = [lr_metrics, rf_metrics]
    save_metrics(metrics_list)
    
    print("\n" + "="*50)
    print("Training completed successfully!")
    print("="*50)

if __name__ == "__main__":
    main()