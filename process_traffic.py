import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, to_date, when ,col

# Path to JDBC driver (update this!)
JDBC_JAR_PATH = "/Users/sakshikhade/Traffic Data Pipleline Project/mysql-connector-j-9.3.0.jar"

spark = SparkSession.builder \
    .appName("TrafficETL") \
    .config("spark.jars", JDBC_JAR_PATH) \
    .getOrCreate()

# MySQL connection details
jdbc_url = "jdbc:mysql://localhost:3306/traffic_data"
connection_props = {
    "user": "root",
    "password": "myPass@1234",  # Update if your root has a password
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Step 1: Read from staging table
df = spark.read.jdbc(url=jdbc_url, table="traffic_staging", properties=connection_props)

# Step 2: Transform
df_transformed = df.withColumn("date", to_date("timestamp")) \
    .groupBy("location", "date") \
    .agg(avg("traffic_volume").alias("avg_volume")) \
   .withColumn("status", when(col("avg_volume") > 300, "High").otherwise("Normal"))

# Step 3: Write to processed table
df_transformed.write.jdbc(
    url=jdbc_url,
    table="traffic_processed",
    mode="append",
    properties=connection_props
)

print("✅ Traffic data processed and saved to traffic_processed table.")

spark.stop()
