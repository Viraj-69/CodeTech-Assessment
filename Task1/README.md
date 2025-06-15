# CodTech Task-1: Big Data Analysis using PySpark

## Objective
Perform big data analysis using PySpark on a sample dataset and generate summary insights.

## Technologies Used
- Apache Spark (PySpark)
- Python

## Files Included
- `big_data_analysis.py` – PySpark script for data processing
- `analysis_summary.txt` – Output file containing processed insights

## Dataset
The script is written to process a sample NYC Taxi data (or any CSV with `fare_amount` and `PULocationID`).

## Features
- Reads CSV data using Spark
- Cleans missing values
- Calculates average fare amount
- Shows total trips per pickup location

## How to Run
```bash
spark-submit big_data_analysis.py
```

## Output
- Summary statistics printed in terminal
- `analysis_summary.txt` with insights