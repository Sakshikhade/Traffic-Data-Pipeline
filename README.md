# Traffic Data Pipeline

A comprehensive end-to-end data pipeline for traffic monitoring, processing, prediction, and visualization using Apache Spark, MySQL, Prophet forecasting, and Python.

## 📊 Project Overview

This project implements a complete traffic data pipeline that:
- Simulates real-time traffic data
- Processes data using Apache Spark
- Stores data in MySQL database
- Predicts future traffic patterns using Prophet
- Generates comprehensive visualizations
- Combines actual and predicted data for analysis

## 🏗️ Architecture

```
Data Simulation → MySQL (Staging) → Spark Processing → MySQL (Processed) → Prophet Forecasting → Visualization
```

## 📁 Project Structure

```
Traffic Data Pipeline Project/
├── simulate_traffic.py          # Generates synthetic traffic data
├── process_traffic.py           # Spark ETL pipeline
├── predict_traffic.py           # Traffic forecasting using Prophet
├── combine_traffic.py           # Merges actual and predicted data
├── visualize_traffic.py         # Data visualization and charts
├── mysql_connection.py          # Database connection testing
├── mysql-connector-j-9.3.0.jar # MySQL JDBC driver
├── traffic_processed.csv        # Processed traffic data
├── predicted_traffic.csv        # Forecasted traffic data
├── traffic_combined.csv         # Combined actual + predicted data
├── traffic_combined.xlsx        # Excel version of combined data
├── *.png                       # Generated charts and visualizations
├── forecasts/                  # Individual location forecast plots
│   ├── Airport Road_forecast.png
│   ├── Bridge_forecast.png
│   ├── Downtown_forecast.png
│   ├── Highway 101_forecast.png
│   ├── Main St_forecast.png
│   └── University Blvd_forecast.png
└── artifacts/                  # Additional project artifacts
```

## 🛠️ Technologies Used

- **Apache Spark**: Large-scale data processing and ETL
- **MySQL**: Data storage and management
- **Prophet**: Time series forecasting
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Python**: Primary programming language

## 📋 Prerequisites

Before running this project, ensure you have:

1. **Python 3.7+** installed
2. **Apache Spark** installed and configured
3. **MySQL Server** running locally
4. Required Python packages (see Installation section)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Traffic Data Pipleline Project"
   ```

2. **Install Python dependencies**
   ```bash
   pip install pandas mysql-connector-python prophet matplotlib pyspark findspark
   ```

3. **Set up MySQL Database**
   ```sql
   CREATE DATABASE traffic_data;
   USE traffic_data;
   
   CREATE TABLE traffic_staging (
       id INT AUTO_INCREMENT PRIMARY KEY,
       location VARCHAR(100),
       timestamp DATETIME,
       traffic_volume INT,
       road_condition VARCHAR(50)
   );
   
   CREATE TABLE traffic_processed (
       id INT AUTO_INCREMENT PRIMARY KEY,
       location VARCHAR(100),
       date DATE,
       avg_volume DOUBLE,
       status VARCHAR(20)
   );
   ```

4. **Configure Database Connection**
   Update the database credentials in all Python files:
   ```python
   connection = mysql.connector.connect(
       host="localhost",
       user="root",
       password="your_password_here",  # Update this
       database="traffic_data"
   )
   ```

## 🎯 Usage

### Step 1: Generate Traffic Data
```bash
python simulate_traffic.py
```
Generates 500 synthetic traffic records across 5 locations with random timestamps, volumes, and road conditions.

### Step 2: Process Data with Spark
```bash
python process_traffic.py
```
- Reads raw data from `traffic_staging` table
- Aggregates daily average traffic volume by location
- Classifies traffic status as "High" (>300) or "Normal"
- Saves processed data to `traffic_processed` table

### Step 3: Generate Forecasts
```bash
python predict_traffic.py
```
- Uses Prophet to forecast traffic for the next 7 days
- Creates individual forecast plots for each location
- Saves predictions to `predicted_traffic.csv`

### Step 4: Combine Data
```bash
python combine_traffic.py
```
Merges actual and predicted traffic data into a single dataset (`traffic_combined.csv`).

### Step 5: Create Visualizations
```bash
python visualize_traffic.py
```
Generates:
- Line chart: Traffic volume trends over time
- Bar chart: Average traffic volume by location
- Pie chart: Traffic status distribution

## 📈 Generated Outputs

### Data Files
- `traffic_processed.csv`: Daily aggregated traffic data
- `predicted_traffic.csv`: 7-day traffic forecasts
- `traffic_combined.csv/xlsx`: Combined actual and predicted data

### Visualizations
- `traffic_trend_line_chart.png`: Time series of traffic volume
- `traffic_volume_bar_chart.png`: Average volume comparison
- `traffic_status_pie_chart.png`: Status distribution
- `forecasts/*.png`: Individual location forecasts

## 📊 Sample Data

The pipeline processes traffic data for these locations:
- Downtown
- Highway 101
- Bridge
- Airport Road
- Main St
- University Blvd

Traffic volume ranges from 50-800 vehicles, with road conditions including Clear, Wet, Foggy, and Construction.

## 🔧 Configuration

### Spark Configuration
The project uses Spark with MySQL JDBC driver. Ensure the JAR path is correct:
```python
JDBC_JAR_PATH = "/path/to/mysql-connector-j-9.3.0.jar"
```

### Prophet Model Settings
- Uses daily seasonality for traffic patterns
- Forecasts 7 days into the future
- Requires minimum 10 data points per location

## 🐛 Troubleshooting

### Common Issues

1. **MySQL Connection Error**
   - Verify MySQL server is running
   - Check credentials and database name
   - Ensure MySQL connector is installed

2. **Spark JDBC Error**
   - Verify JDBC JAR path is correct
   - Check MySQL driver compatibility
   - Ensure Spark is properly installed

3. **Prophet Installation Issues**
   - Install using: `pip install prophet`
   - On macOS: May need `brew install cmake`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or issues, please create an issue in the repository or contact the maintainer.

---

**Note**: This project is designed for educational and demonstration purposes. For production use, consider additional error handling, security measures, and scalability optimizations.
