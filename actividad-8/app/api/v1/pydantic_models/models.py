from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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
