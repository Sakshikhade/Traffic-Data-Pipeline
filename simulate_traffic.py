import mysql.connector
import random
from datetime import datetime, timedelta

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="myPass@1234",
    database="traffic_data"
)

cursor = connection.cursor()

locations = ['Downtown', 'Highway 101', 'Bridge', 'Airport Road', 'Main St']
# Generate a random date between Jan 1 and Dec 31, 2023
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

for _ in range(500):
    location = random.choice(locations)
    traffic_volume = random.randint(50, 800)
    road_condition = random.choice(['Clear', 'Wet', 'Foggy', 'Construction'])

    random_days = random.randint(0, (end_date - start_date).days)
    timestamp = start_date + timedelta(days=random_days, hours=random.randint(0, 23), minutes=random.randint(0, 59))

    cursor.execute("""
        INSERT INTO traffic_staging (location, timestamp, traffic_volume, road_condition)
        VALUES (%s, %s, %s, %s)
    """, (location, timestamp, traffic_volume, road_condition))

connection.commit()
cursor.close()
connection.close()
print("✅ Inserted 1000 rows across multiple locations and dates")
