# FastAPI + Azure Data Lake Ingestion

This app shows how to:
- Accept POSTed JSON using FastAPI + Pydantic
- Validate schema with Pydantic
- Store data in Azure Data Lake Gen2

### Run Locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
./run.sh

### ⚡ FastAPI Azure Data Lake Ingestion Service
This project demonstrates a scalable, cloud-native ingestion service built with FastAPI, Pydantic, and Azure Data Lake Gen2.

Designed for enterprise data engineering use cases—like those seen in Accenture client engagements—this service enables:

✅ Secure ingestion of external JSON payloads via REST API

✅ Schema validation using Pydantic

✅ Raw data storage in Azure Data Lake Gen2

✅ IaC deployment via Terraform (resource group, storage, filesystem)

✅ Containerization using Docker & Docker Compose

This architecture fits cleanly into modern data platforms built on Azure, providing a clean staging point for downstream analytics in Synapse, Databricks, or Power BI.

🔧 Tech Stack: FastAPI · Python · Azure Storage SDK · Terraform · Docker
🌐 Use Case: Multi-vendor JSON ingestion for enterprise data lake systems
📦 Deployable: Locally via Docker or to Azure Web App Containers

👷‍♂️ Built for real-world client environments like those served by Accenture’s Intelligent Platform Services team.
