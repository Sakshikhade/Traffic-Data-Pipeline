import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="myPass@1234",  # ← Replace with your MySQL password
    database="traffic_data"
)

# Load data
query = "SELECT * FROM traffic_processed"
df = pd.read_sql(query, conn)
conn.close()

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# 1. Line chart – Traffic volume trend per location
plt.figure(figsize=(10, 5))
for location in df['location'].unique():
    subset = df[df['location'] == location]
    plt.plot(subset['date'], subset['avg_volume'], marker='o', label=location)

plt.title("Traffic Volume Over Time (per Location)")
plt.xlabel("Date")
plt.ylabel("Average Volume")
plt.legend()
plt.tight_layout()
plt.savefig("traffic_trend_line_chart.png")
plt.show()

# 2. Bar chart – Average volume per location
plt.figure(figsize=(8, 5))
avg_by_location = df.groupby('location')['avg_volume'].mean().sort_values()
avg_by_location.plot(kind='bar', color='skyblue')
plt.title("Average Traffic Volume by Location")
plt.ylabel("Avg Volume")
plt.tight_layout()
plt.savefig("traffic_volume_bar_chart.png")
plt.show()

# 3. Pie chart – Traffic status distribution
status_counts = df['status'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Traffic Status Distribution")
plt.tight_layout()
plt.savefig("traffic_status_pie_chart.png")
plt.show()
df.to_csv("traffic_processed.csv", index=False)
print("✅ CSV exported successfully.")

