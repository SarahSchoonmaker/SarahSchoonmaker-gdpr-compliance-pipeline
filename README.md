# GDPR Data Engineering & LLM Automation Pipeline

This project builds a scalable data engineering pipeline to analyze and automate compliance review of SQL logs, focusing on GDPR-sensitive data detection. The system integrates real-time ingestion (Kafka), transformation (Spark, dbt), orchestration (Airflow), and automation using LLMs to flag personal data references in SQL logs.

---

## 📦 PHASE 1: Data Ingestion & Setup

**Goal:** Ingest GDPR violation dataset and prepare it for processing in the pipeline.

### ✅ Components:

- Download dataset from Kaggle (`jessemostipak/gdpr-violations`)
- Load and preview data with `pandas`
- Upload the dataset to AWS S3
- Lay groundwork for transformation and analysis

### 📁 Files:

- `get_dataset.py`: Downloads GDPR dataset using `kagglehub`
- `upload_to_s3.py`: Uploads the dataset to an S3 bucket
- `.env`: Stores Kaggle API credentials securely
- `requirements.txt`: Python dependencies

---

## ⚙️ PHASE 2: Pipeline Orchestration & Modeling

**Goal:** Build a data pipeline to clean, structure, and schedule processing jobs.

### ✅ Components:

- **Apache Spark**: Processes raw SQL logs from S3 or Kafka
- **dbt (Data Build Tool)**: Applies layered SQL transformations with testing
- **Apache Airflow**: Orchestrates ingestion → transformation → LLM automation

### 💡 Workflow:

1. Ingest streaming logs from Kafka
2. Clean and enrich data with Spark
3. Load to warehouse (Redshift or Postgres)
4. Use `dbt` to model and validate
5. Trigger flow with Airflow DAGs

---

## 🤖 PHASE 3: LLM + NLP Automation

**Goal:** Automatically flag GDPR-sensitive fields in SQL queries using LLMs or NLP.

### ✅ Components:

- Use OpenAI's GPT or `sqlparse` + spaCy
- Scan SQL logs for risky fields like `email`, `ip_address`, `ssn`, `location`
- Generate logs or alerts for compliance review
- Visualize or store results in dashboard or S3/DB

### 🧠 Sample Prompt:

> "Analyze this SQL query and flag any GDPR-sensitive fields: `SELECT user_id, email, ip_address FROM users;`"

---

## 🚀 Technologies Used

- **Python** & **Pandas**
- **AWS (S3, Athena, Glue, Redshift)**
- **Apache Kafka** – real-time ingestion
- **Apache Spark** – batch/stream processing
- **dbt** – data modeling & testing
- **Apache Airflow** – workflow orchestration
- **OpenAI / LangChain** – LLM for SQL audit automation

---

## 🧰 Setup

```bash
# Install dependencies
python -m pip install -r requirements.txt

# Configure Kaggle
Place credentials in .env:
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_key

# Download GDPR dataset
python get_dataset.py

# Upload to S3
python upload_to_s3.py
```

# GDPR Compliance Analytics Pipeline

This project builds an end-to-end data pipeline on AWS to ingest, analyze, and visualize GDPR violation data using Athena, Lambda, Glue, and QuickSight. It enables organizations to monitor and understand compliance trends, uncover risk patterns, and communicate regulatory exposure through interactive dashboards.

---

## 🎯 Project Purpose

This pipeline analyzes structured GDPR enforcement data combined with the legal articles and summaries describing each violation. It helps uncover:

- Common patterns in GDPR article violations
- Regulatory behavior across EU countries and data protection authorities
- Severity of fines by category or article type
- How violations align with specific GDPR chapters and legal language

The project uses AWS Glue, Athena, Lambda, and QuickSight to automate ingestion, analysis, and visualization. It's ideal for privacy teams, policy researchers, and compliance officers looking to gain insights from real-world GDPR enforcement data.

---

## 📊 Pipeline Architecture

| Stage          | Service           | Description                                                       |
| -------------- | ----------------- | ----------------------------------------------------------------- |
| **Ingest**     | S3 + Lambda       | GDPR CSVs uploaded to S3 trigger Athena queries via Lambda        |
| **Catalog**    | AWS Glue          | Crawler scans CSV and registers schema in Glue Data Catalog       |
| **Query**      | Amazon Athena     | Serverless SQL queries extract insights from violation data       |
| **Automation** | AWS Lambda        | Scheduled or event-based Lambda runs SQL queries and logs results |
| **Visualize**  | Amazon QuickSight | Dashboards display violation patterns, trends, and top fines      |

---

## 📕 Key Features

- Automated trigger on CSV upload
- Lambda executes Athena queries for violations > €1M
- Glue Crawler dynamically detects schema
- QuickSight visualizes high-risk areas and fine distribution
- Fully serverless and scalable using AWS-native services

---

## 📊 Example Insights

- Top 10 GDPR fines by organization and country
- Violation counts grouped by article (e.g., Article 6, Article 13)
- Trend of GDPR enforcement actions over time
- Heatmap of fines by country or region

---

## 🚀 Getting Started

### Prerequisites

- AWS account with permissions to use S3, Glue, Athena, Lambda, QuickSight
- `kaggle.json` API token (for optional data download step)

### Deployment Steps

1. Upload GDPR dataset to S3 (`s3://gdpr-data-kaggle/`)
2. Configure and run a Glue Crawler to create `gdpr_db.gdpr_data_kaggle`
3. Create a Lambda function with IAM role (`AmazonAthenaFullAccess`, `AmazonS3ReadOnlyAccess`)
4. Add S3 and/or CloudWatch triggers to Lambda
5. Connect QuickSight to Athena and visualize query results

---

## 🌐 Why QuickSight?

QuickSight is tightly integrated with Athena and Glue, making it the perfect tool for:

- Building real-time dashboards from query results
- Sharing visual reports with compliance and executive teams
- Scheduling regular data refreshes from S3/Athena

---

## 🚧 Sample Athena Query (Used in Lambda)

```sql
SELECT company, fine_amount, violation_type, date
FROM gdpr_data_kaggle
WHERE fine_amount > 1000000
ORDER BY fine_amount DESC
LIMIT 10;
```

## Quicksight visualization

![Alt Text](gdpr-pie-charg.png)
