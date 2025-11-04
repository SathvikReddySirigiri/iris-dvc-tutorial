from sklearn.datasets import load_iris
import pandas as pd

# Load iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# Save to CSV
df.to_csv('data/iris.csv', index=False)
print(f"Dataset created with {len(df)} samples")
print(df['species'].value_counts())