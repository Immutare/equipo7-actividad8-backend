import datetime
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QueryBase(BaseModel):
    request: str
    response: Optional[str] = None

class QueryCreate(QueryBase):
    pass

class QueryUpdate(QueryBase):
    request: Optional[str] = None
    response: Optional[str] = None
    datecreated: Optional[datetime] = None
    pass

class Query(QueryBase):
    id: int
    datecreated: datetime

    class Config:
        orm_mode = True
