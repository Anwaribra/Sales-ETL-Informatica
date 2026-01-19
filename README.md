# Sales ETL Pipeline using Informatica


This project demonstrates an **end-to-end ETL pipeline built using Informatica PowerCenter**.
The pipeline extracts sales data from multiple sources, applies business transformations, and loads the processed data into a data warehouse for analytics and reporting.


## Features

* Build an automated ETL pipeline using Informatica
* Integrate data from heterogeneous sources
* Apply data cleansing, validation, and transformation rules
* Load clean and aggregated data into a data warehouse
* Enable analytics and reporting on sales performance

---

<!-- ##  Architecture

**Source → Informatica → Data Warehouse → BI Tool** -->

<!-- * **Sources**

  * CSV files (Daily Sales Data)
  * Relational Database (Customers & Products)

* **ETL Tool**

  * Informatica PowerCenter

* **Target**

  * Data Warehouse (PostgreSQL)

* **Visualization**

  * Power BI -->

<!-- 
---

## 📂 Project Structure

```
sales-etl-informatica/
│
├── sources/
│   ├── sales_data.csv
│   └── customers.sql
│
├── mappings/
│   ├── m_sales_cleaning
│   ├── m_sales_enrichment
│   └── m_sales_aggregation
│
├── workflows/
│   ├── wf_sales_etl
│   └── wf_sales_aggregation
│
├── targets/
│   ├── sales_cleaned
│   └── sales_summary
│
└── documentation/
    └── README.md
``` -->
<!-- 
---

##  ETL Workflow Details

### Data Extraction

* Extract sales transactions from CSV files
* Extract customer and product data from relational databases

###  Data Transformation

* Remove null and invalid records
* Standardize date and currency formats
* Join sales with customer and product data
* Calculate KPIs:

  * Total Sales
  * Revenue per Customer
  * Product-wise Revenue
* Categorize customers based on spending behavior

###  Data Loading

* Load cleansed data into staging tables
* Load aggregated data into fact and summary tables

---

##  Informatica Components Used

* Source Qualifier
* Expression Transformation
* Lookup Transformation
* Filter Transformation
* Aggregator Transformation
* Router Transformation
* Workflow Manager
* Workflow Monitor

---

##  Scheduling & Monitoring

* Workflows scheduled for daily execution
* Error handling and logging enabled
* Failed records captured for reprocessing

---

##  Sample Use Cases

* Sales performance analysis
* Customer segmentation
* Product revenue insights
* Business reporting and dashboards -->
