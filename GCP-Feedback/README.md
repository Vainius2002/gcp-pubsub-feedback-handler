# GCP Feedback Ingestion

This project demonstrates a simple cloud-based feedback ingestion pipeline using **Google Cloud Pub/Sub**, **Python**, and **PostgreSQL**. It listens for user feedback messages published to a Pub/Sub topic and stores them in a PostgreSQL database hosted on Google Cloud SQL.

## 🧠 Purpose

The goal of this project is to showcase practical experience with:
- Google Cloud Platform (GCP)
- Pub/Sub message consumption using `google-cloud-pubsub`
- Cloud SQL integration (PostgreSQL)
- Python-based microservices
- (Optional) BigQuery integration for analytics

## 📦 Tech Stack

- Python 3
- Google Cloud Pub/Sub
- PostgreSQL (Cloud SQL)
- psycopg2 (PostgreSQL client for Python)
- `google-cloud-pubsub` Python library

## 📤 Flow Summary

1. A message (JSON-formatted feedback) is published to a Pub/Sub topic.
2. The subscriber (this app) listens to the topic and receives the message.
3. It extracts the `username`, `message`, and `timestamp` fields.
4. The data is stored in a PostgreSQL database.

## 📁 Example Pub/Sub Message

```json
{
  "username": "Vainius Lunys",
  "message": "Very well made. I give it a 10!",
  "timestamp": "2025-07-23T17:12:00Z"
}

## ✅ Features
    1. Reconnects to PostgreSQL per message (to simulate stateless design).
    2. Converts and validates ISO timestamps.
    3. Handles and logs insertion errors.
    4. (Optional extension) Can be connected to BigQuery for analytics and dashboarding.

🛠️ Setup Instructions
1. Enable required GCP services
   1) Pub/Sub
   2) Cloud SQL (PostgreSQL)
   3) IAM & Admin for role assignment

2. Install Python dependencies
   pip install google-cloud-pubsub psycopg2

3. Set up authentication (Export your service account key):
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
   
4. Run the subscriber script
