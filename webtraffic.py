# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the uploaded CSV
df = pd.read_csv('traffic.csv')

# Step 3: Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Step 4: Print summary
print("📊 Website Traffic Summary:\n")
print(df.describe())

# Step 5: Line plot - Visitors over time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Visitors'], marker='o', color='blue')
plt.title('Visitors Over Time')
plt.xlabel('Date')
plt.ylabel('Visitors')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 6: Bar chart - Page views
plt.figure(figsize=(10, 5))
plt.bar(df['Date'], df['PageViews'], color='green')
plt.title('Page Views Over Time')
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.tight_layout()
plt.show()
# Step 7: Bounce rate trend
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Date', y='BounceRate', color='red', marker='o')
plt.title('Bounce Rate Trend')
plt.ylabel('Bounce Rate (%)')
plt.xlabel('Date')
plt.tight_layout()
plt.show()

# Step 8: Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df[['Visitors', 'BounceRate', 'PageViews']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Metrics')
plt.tight_layout()
plt.show()