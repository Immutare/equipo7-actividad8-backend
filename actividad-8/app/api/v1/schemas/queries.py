from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QueryBase(BaseModel):
    naturallanguagerequest: str
    response: Optional[str] = None

class QueryCreate(QueryBase):
    pass

class Query(QueryBase):
    idqueries: int
    timeofrequest: datetime

    class Config:
        orm_mode = True
