import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Step 1: Sample movie data
data = {
    'Title': [
        'Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E',
        'Movie F', 'Movie G', 'Movie H', 'Movie I', 'Movie J'
    ],
    'Duration': [90, 95, 150, 160, 170, 200, 100, 105, 110, 210],
    'Rating': [7.0, 6.8, 8.5, 8.7, 8.6, 9.0, 6.5, 6.7, 6.9, 9.1],
    'Year': [2000, 2002, 2010, 2011, 2012, 2015, 2003, 2005, 2006, 2016]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Step 2: Feature scaling
X = df[['Duration', 'Rating', 'Year']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply DBSCAN
db = DBSCAN(eps=1.2, min_samples=2)  # adjust eps for sensitivity
df['Cluster'] = db.fit_predict(X_scaled)

# Step 4: Display results
print("\nClustered Movies:")
print(df[['Title', 'Duration', 'Rating', 'Year', 'Cluster']])

# Step 5: Visualize clusters
plt.figure(figsize=(8, 6))
plt.scatter(df['Duration'], df['Rating'], c=df['Cluster'], cmap='rainbow', s=100)
plt.xlabel('Duration (min)')
plt.ylabel('IMDb Rating')
plt.title('Movie Clustering using DBSCAN')
for i, title in enumerate(df['Title']):
    plt.annotate(title, (df['Duration'][i]+1, df['Rating'][i]+0.05), fontsize=8)
plt.grid(True)
plt.show()
