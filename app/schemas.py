from pydantic import BaseModel, Field
from typing import Optional

class Record(BaseModel):
    id: int = Field(..., example=123)
    name: str = Field(..., example="Jay")
    email: Optional[str] = Field(None, example="jay@example.com")
