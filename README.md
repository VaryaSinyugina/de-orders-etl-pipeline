# Orders ETL Pipeline (Airflow)

## Overview

This project demonstrates a complete data engineering pipeline built with Apache Airflow.

The pipeline:

* extracts order data from a CSV file
* transforms and cleans the data
* performs data quality checks
* loads the data into PostgreSQL

It reflects real-world data engineering practices including orchestration, debugging, and environment setup.

---

## Architecture

```
CSV (raw data)
    ↓
Extract (pandas)
    ↓
Transform (data cleaning)
    ↓
Quality Checks
    ↓
Load (PostgreSQL)
    ↓
Orchestration (Airflow DAG)
```

---

## Tech Stack

* Python
* Apache Airflow
* PostgreSQL
* Pandas
* SQLAlchemy
* WSL (Linux environment on Windows)

---

## Project Structure

```
de-orders-etl-pipeline/
│
├── data/
│   └── raw/
│       └── orders.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── quality_checks.py
│   └── etl.py
│
├── dags/
│   └── orders_etl_dag.py
│
├── sql/
│   └── create_table.sql
│
├── requirements.txt
└── README.md
```

---

## How It Works

Airflow runs a DAG that triggers the ETL pipeline:

1. Extract
   Reads raw data from CSV using pandas

2. Transform
   Cleans and prepares the dataset

3. Quality Checks
   Ensures data consistency (for example, no null values in `order_id`)

4. Load
   Inserts data into PostgreSQL

---

## How to Run

### 1. Clone repository

```
git clone https://github.com/YOUR_USERNAME/de-orders-etl-pipeline.git
cd de-orders-etl-pipeline
```

---

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Database Setup

Make sure PostgreSQL is installed and running.

Create database:

```
CREATE DATABASE de_first_pet_project;
```

Run SQL script to create the table:

```
-- execute sql/create_table.sql
```

---

## Environment Variables

Set database credentials before running the project.

For Linux / WSL:

```
export DB_USER=de_user
export DB_PASSWORD=12345
export DB_NAME=de_first_pet_project
```

For Windows (PowerShell):

```
setx DB_USER de_user
setx DB_PASSWORD 12345
setx DB_NAME de_first_pet_project
```

The project uses environment variables for database configuration instead of hardcoded credentials.

---

## Running Airflow

Start Airflow:

```
airflow standalone
```

Open UI:

```
http://localhost:8080
```

Run pipeline:

* Find DAG `orders_etl_pipeline`
* Enable it
* Trigger DAG manually

---

## Data Quality Checks

The pipeline validates:

* dataset is not empty
* no null values in key fields

---

## Important Notes

* The project uses dynamic paths instead of hardcoded directories to ensure portability
* Airflow runs tasks from a different working directory, so relative paths may not work
* PostgreSQL is a system dependency and is not included in requirements.txt
