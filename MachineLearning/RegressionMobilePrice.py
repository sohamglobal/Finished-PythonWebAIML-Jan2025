import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Sample data
data = {
    'RAM': [2, 3, 4, 6, 8],
    'Price': [5, 7, 9, 13, 17]  # Price in ₹1000s
}
df = pd.DataFrame(data)

# Step 2: Features and labels
X = df[['RAM']]   # Independent variable (2D)
y = df['Price']   # Dependent variable (target)

# Step 3: Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 4: Predict price for new RAM values
ram_values = [[5], [7]]
predicted_prices = model.predict(ram_values)

print("Predicted Prices:")
for ram, price in zip(ram_values, predicted_prices):
    print(f"RAM: {ram[0]} GB → ₹{round(price, 2)}K")

# Step 5: Plot
plt.scatter(df['RAM'], df['Price'], color='blue', label='Actual Data')
plt.plot(df['RAM'], model.predict(X), color='red', label='Regression Line')
plt.xlabel('RAM (GB)')
plt.ylabel('Price (₹1000s)')
plt.title('Mobile Price Prediction using Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
