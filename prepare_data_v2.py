from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

# Load iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# Augment data with slight variations
np.random.seed(42)
augmented_data = []

for _, row in df.iterrows():
    # Add noise to create augmented samples
    noise = np.random.normal(0, 0.1, 4)
    new_row = row.copy()
    new_row[iris.feature_names] += noise
    augmented_data.append(new_row)

augmented_df = pd.DataFrame(augmented_data)

# Combine original and augmented
df_v2 = pd.concat([df, augmented_df], ignore_index=True)

# Save to CSV
df_v2.to_csv('data/iris.csv', index=False)
print(f"Dataset created with {len(df_v2)} samples")
print(df_v2['species'].value_counts())