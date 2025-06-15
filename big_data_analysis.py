from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.appName("BigDataAnalysis").getOrCreate()
data = spark.read.csv("sample_data.csv", header=True, inferSchema=True)

# Drop nulls
data_cleaned = data.dropna()

# Trip count by location
trip_counts = data_cleaned.groupBy("PULocationID").count()

# Average fare amount
avg_fare = data_cleaned.select(avg(col("fare_amount"))).first()[0]

with open("analysis_summary.txt", "w") as f:
    f.write(f"Total Trips by Location:\n{trip_counts.collect()}\n\n")
    f.write(f"Average Fare Amount: {avg_fare:.2f}")

spark.stop()