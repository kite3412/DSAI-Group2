Data Warehouse and ELT Pipeline Report for Olist Data
1. Overview
This project transformed raw Olist e-commerce data into a star schema data warehouse using DuckDB and dbt. We then leveraged Python (with Pandas and Seaborn) for data quality testing, exploratory analysis, and visualization. The objective was to create an efficient, scalable pipeline that delivers clean, enriched data for BI analysts and data scientists.

2. Technical Approach
2.1 Tool Selection
DuckDB:

Why DuckDB?
DuckDB is an in-process SQL OLAP database designed for fast analytical queries. It supports SQL standards, runs on a local machine without heavy configuration, and integrates well with Python.

Alternatives Considered:
While tools like SQLite or PostgreSQL were considered, DuckDB was chosen for its performance with large analytical queries and its ease of deployment.

dbt (Data Build Tool):

Why dbt?
dbt simplifies ELT pipelines by enabling modular SQL development, version control, and built-in testing. It supports transforming raw data into staging, dimension, and fact models.

Alternatives Considered:
Custom Python scripts and other ETL frameworks were considered, but dbt's modular approach and built-in documentation and testing features were particularly attractive.

Python with Pandas and Seaborn:

Why Python?
Python’s rich ecosystem makes it ideal for data manipulation (Pandas) and visualization (Seaborn, Matplotlib). This combination allows for rapid exploratory data analysis and the creation of insightful charts.

Alternatives Considered:
Tools like R or BI platforms (Tableau, Power BI) were options for visualization; however, Python provided a seamless integration with our ELT pipeline and the database.

2.2 Schema Design: Star Schema
Our data warehouse uses a star schema, which consists of:

Fact Table (FactSales):
Contains transactional data such as order details, prices, freight costs, and derived measures like total sale amount.

Dimension Tables:

DimCustomer: Contains customer attributes (ID, unique identifier, city, state, zip code).

DimProduct: Contains product attributes (ID, category, weight, dimensions).

DimDate: A calendar table with date, day, month, quarter, and year attributes.

(Optional) DimSeller: Contains seller location and other attributes.

Schema Design Justification
Efficiency in Querying:
The star schema is optimized for analytical queries. Denormalization into a single fact table and multiple dimensions minimizes the number of joins required and simplifies aggregation.

Flexibility:
Dimensions can be extended or enriched over time (e.g., adding customer segmentation or product hierarchies) without altering the fact table.

Performance:
Analytical databases like DuckDB can quickly scan and aggregate data in a star schema, which is essential for reporting and BI workloads.

3. ELT Pipeline Implementation
3.1 Data Transformation with dbt
Staging Models:
Raw CSV files are loaded and lightly transformed (e.g., trimming text, casting data types) in staging models (e.g., stg_customers.sql, stg_orders.sql, stg_order_items.sql, stg_order_reviews.sql).

Dimension and Fact Models:
From the staging layer, we build dimension tables (dim_customer, dim_product, dim_date) and a fact table (fact_sales) that aggregates orders, order items, and integrates order payment details.

Data Quality Testing:
Built-in tests in dbt (and optionally Great Expectations) ensure non-null values, uniqueness, and referential integrity. These tests are defined in YAML files alongside models.

3.2 Derived Columns
In our fact table (fact_sales), derived columns such as total_sale_amount are computed by summing the price and freight value. Additional metrics like customer lifetime value can be calculated in separate aggregation models.

4. Data Analysis and Visualization
After the data warehouse was built, we connected to DuckDB using SQLAlchemy and performed exploratory analysis with Pandas. Key insights were visualized using Seaborn and Matplotlib. Below are some representative visualizations:

4.1 Monthly Sales Trends by Product Category
Figure 1: Lineplot showing monthly sales trends, segmented by product category.
This visualization reveals seasonality and category-specific trends, which are crucial for forecasting and inventory management.

4.2 Average Freight Cost by Customer State
Figure 2: Barplot of average freight cost by state.
Identifies regions where shipping costs are higher, guiding logistics optimization and potential pricing strategy adjustments.

4.3 Distribution of Review Scores by Product Category
Figure 3: Boxplot of review score distributions across product categories.
Highlights product quality and customer satisfaction variances, helping prioritize improvements or promotional efforts.

4.4 Payment Type vs. Average Order Value
Figure 4: Barplot comparing average order value across different payment types.
Insights into customer behavior based on payment preferences, which can inform marketing and discount strategies.

4.5 Shipping Time Analysis
Figure 5: Histogram with KDE for shipping times (in days).
Displays the distribution of shipping times, helping identify outliers and opportunities to improve delivery performance.

5. Key Findings and Insights
Sales Trends:
Analysis of monthly sales by product category revealed clear seasonal trends and identified categories driving revenue growth.

Regional Variations:
The average freight cost analysis showed that certain regions incur higher shipping expenses, suggesting the need for logistics optimization.

Customer Feedback:
Review score distributions vary significantly across product categories, providing actionable insights into product quality.

Payment Preferences:
Different payment types correlate with varying average order values, indicating distinct customer segments.

Operational Efficiency:
Shipping time analysis pinpointed potential delays, guiding operational improvements to enhance customer satisfaction.

6. Conclusion
The technical approach—leveraging DuckDB, dbt, and Python—enabled us to build a robust and efficient ELT pipeline. The star schema design supports efficient querying and scalability, while the combination of dbt for transformation and Python for analysis provides a flexible, maintainable solution. These insights empower business stakeholders to make data-driven decisions to optimize sales, logistics, and customer engagement.

