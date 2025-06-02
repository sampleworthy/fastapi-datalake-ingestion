from fastapi import FastAPI, HTTPException
from app.schemas import Record
from app.datalake import upload_json_data
import json
from datetime import datetime

app = FastAPI()

@app.post("/submit")
def submit_data(record: Record):
    try:
        payload = json.dumps(record.dict(), indent=2)
        timestamp = datetime.utcnow().isoformat()
        filename = f"{record.id}_{timestamp}.json"
        upload_json_data(filename, payload)
        return {"message": "Data uploaded to Azure Data Lake", "file": filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
