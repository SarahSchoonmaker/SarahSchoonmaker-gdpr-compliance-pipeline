# GDPR Compliance Analytics Pipeline

This project builds an end-to-end data pipeline on AWS to ingest, analyze, and visualize GDPR violation data using Athena, Lambda, Glue, and QuickSight. It enables organizations to monitor and understand compliance trends, uncover risk patterns, and communicate regulatory exposure through interactive dashboards.

---

## 🌟 Project Purpose

GDPR imposes strict requirements on how personal data is collected, processed, and stored. Non-compliance can lead to fines in the millions. The goal of this project is to:

- Automatically ingest GDPR violations data from public sources
- Detect high-risk violation types and trends
- Visualize top offending countries, authorities, and companies
- Enable compliance teams to act on real-time insights

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

## .env

<pre> ``` KAGGLE_USERNAME= KAGGLE_KEY= AWS_ACCESS_KEY_ID= AWS_SECRET_ACCESS_KEY= AWS_REGION= ``` </pre>

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

## 📊 Future Enhancements

- Integrate LLMs to scan SQL logs for GDPR-sensitive fields
- Add Redshift as a long-term data store
- Enable Slack/email alerts for violations over thresholds
- Create role-based QuickSight dashboards (Compliance, Legal, Exec)

---

## 🚧 Sample Athena Query (Used in Lambda)

```sql
SELECT company, fine_amount, violation_type, date
FROM gdpr_data_kaggle
WHERE fine_amount > 1000000
ORDER BY fine_amount DESC
LIMIT 10;
```

---

## Quicksight visualization

![Alt Text](gdpr-pie-charg.png)
