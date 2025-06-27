import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Step 1: Create data
data = {
    'ScreenSize': [6.0, 5.5, 15.6, 14.0, 6.5, 13.3],
    'RAM': [4, 3, 8, 16, 6, 8],
    'Device': ['Mobile', 'Mobile', 'Laptop', 'Laptop', 'Mobile', 'Laptop']
}

df = pd.DataFrame(data)

# Step 2: Features and labels
X = df[['ScreenSize', 'RAM']]
y = df['Device']

# Step 3: Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Step 4: Predict new data
new_data = pd.DataFrame({'ScreenSize': [6.2, 14.0], 'RAM': [4, 12]})
predictions = model.predict(new_data)

print("Predictions:")
print(new_data.assign(Predicted_Device=predictions))
