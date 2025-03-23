# Data Pipeline Architecture and Documentation Report

## 1. Overview

This document describes the architecture of our data pipeline system, including:
- **Code Documentation:** How our SQL models and Python scripts are organized and documented.
- **Data Lineage:** The flow of data from raw source files into a star schema via dbt.
- **Pipeline Architecture:** A high-level diagram and explanation of how data moves from ingestion through transformation to analytics.

---

## 2. Code Documentation

### 2.1 dbt Models

Our dbt project is structured to implement an ELT pipeline that transforms raw CSV data into a star schema. Each model is well-documented with inline comments and configuration metadata.

#### Example: `stg_customers.sql`

```sql
{{ config(materialized='table') }}

-- This staging model cleans the raw customers data.
-- It trims extra spaces from text columns and converts types where necessary.
SELECT
    customer_id,
    customer_unique_id,
    TRIM(customer_city) AS city,        -- Clean city name
    TRIM(customer_state) AS state,       -- Clean state name
    CAST(customer_zip_code_prefix AS INTEGER) AS zip_code  -- Convert ZIP code to integer
FROM {{ source('olist', 'customers') }}


Example: dim_customer.sql

{{ config(materialized='view') }}

-- This dimension model builds a clean customer dimension.
-- It generates a surrogate key (customer_key) and ensures consistency of customer attributes.
SELECT
    ROW_NUMBER() OVER (ORDER BY customer_id) AS customer_key,  -- Surrogate key generation
    customer_id,
    customer_unique_id,
    TRIM(city) AS city,
    TRIM(state) AS state,
    CAST(zip_code AS INTEGER) AS zip_code
FROM {{ ref('stg_customers') }}

Example: fact_sales.sql

3. Data Lineage
3.1 Data Flow Diagram
Below is a high-level diagram illustrating data lineage:
[Raw CSV Files]
      │
      ▼
┌───────────────────────────┐
│     Raw Data Ingestion    │
│ (e.g., olist_customers,   │
│  olist_orders, etc.)      │
└───────────────────────────┘
      │
      ▼
┌───────────────────────────┐
│    Staging Models (stg)   │
│ - stg_customers.sql       │
│ - stg_orders.sql          │
│ - stg_order_items.sql     │
│ - stg_order_payments.sql  │
│ - stg_order_reviews.sql   │
└───────────────────────────┘
      │
      ▼
┌─────────────────────────────┐
│    Dimensional Models       │
│ - dim_customer.sql          │
│ - dim_product.sql           │
│ - dim_date.sql              │
│   (and optionally dim_seller)│
└─────────────────────────────┘
      │
      ▼
┌─────────────────────────────┐
│      Fact Models            │
│ - fact_sales.sql (with       │
│   integrated payment data)  │
└─────────────────────────────┘
      │
      ▼
[Data Warehouse in DuckDB]
      │
      ▼
┌─────────────────────────────┐
│     Data Analysis &         │
│     Visualization           │
│ - Python (Pandas, Seaborn)   │
│ - BI Tools (Optional)        │
└─────────────────────────────┘


3.2 Data Flow Explanation
Raw CSV Files:
The starting point is a set of CSV files containing raw data (e.g., customers, orders, order items, reviews, payments).

Staging Models:
These models clean and lightly transform the raw data by trimming text, converting data types, and filtering out invalid records.

Dimensional and Fact Models:
Using the staging data, we construct a star schema:

Dimension Tables: Provide descriptive attributes (e.g., customer details in dim_customer, product details in dim_product, and date attributes in dim_date).

Fact Table: fact_sales aggregates transactional data and includes derived metrics (e.g., total sale amount) and integrated payment details.

Data Warehouse:
The transformed tables reside in a DuckDB database optimized for analytical queries.

Data Analysis & Visualization:
Python (with Pandas and Seaborn) is used to connect to DuckDB, perform exploratory analysis, and produce charts/graphs. The processed data is also available for BI tools if further reporting is needed.

4. Pipeline Architecture
4.1 Tools and Their Roles
DuckDB:
Acts as the central data warehouse, providing an in-process SQL engine optimized for OLAP queries.

dbt (Data Build Tool):
Orchestrates the ELT pipeline by transforming raw data into staging, dimension, and fact models. It enforces modular, testable SQL transformations.

Python (Pandas & Seaborn):
Used for data analysis, exploration, and visualization. SQLAlchemy connects Python to DuckDB, while Pandas and Seaborn create dashboards and plots that surface business insights.

4.2 Pipeline Architecture Diagram
Below is a simplified architecture diagram:

           +---------------------+
           | Raw Data (CSV files)|
           +---------------------+
                     │
                     ▼
           +---------------------+
           |  Data Ingestion     |   (Load raw files into DuckDB)
           +---------------------+
                     │
                     ▼
           +---------------------+
           |       dbt           |
           |  (staging, dims,    |
           |   facts models)     |
           +---------------------+
                     │
                     ▼
           +---------------------+
           |    DuckDB Data      |
           |    Warehouse        |
           +---------------------+
                     │
                     ▼
           +---------------------+
           | Data Analysis &     |
           | Visualization (Python)|
           +---------------------+


4.3 Key Architectural Considerations
Modularity:
Using dbt allows each transformation to be modular. This means changes to one model (e.g., stg_orders) do not affect others as long as the interface (columns, keys) remains consistent.

Scalability:
The star schema is designed for fast aggregations and efficient querying, supporting high query performance even as data volumes grow.

Maintainability:
The use of dbt and a clear data lineage ensures that data transformations are documented and testable. This makes it easier for the team to understand and maintain the pipeline over time.

Flexibility for Analysis:
With a clean data warehouse and Python-based visualization, analysts and stakeholders can quickly generate insights (e.g., sales trends, customer segmentation) without waiting for slow, manual ETL processes.

5. Conclusion
This report outlines a robust data pipeline architecture that starts with raw data ingestion and culminates in actionable insights via a star schema design. Tools like DuckDB, dbt, and Python are integrated to ensure the pipeline is modular, scalable, and easy to maintain. Detailed documentation, data lineage diagrams, and pipeline architecture diagrams provide a clear roadmap of how data flows through the system—from ingestion, through transformation, to analysis—empowering business stakeholders to make data-driven decisions.

Appendix
Code Repository: All SQL models and Python scripts are version-controlled in our Git repository.

Data Docs: Use dbt docs generate and dbt docs serve to view interactive documentation of our models and lineage.

Monitoring: Automated tests via dbt and scheduled Python scripts ensure data quality and timely insights.

---

To download this file, copy the content above into a text editor and save it as `Data_Pipeline_Architecture_Report.md`.
