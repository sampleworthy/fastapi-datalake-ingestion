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
