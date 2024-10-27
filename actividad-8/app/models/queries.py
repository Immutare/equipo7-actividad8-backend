import datetime
from sqlalchemy import Column, Integer, Text, TIMESTAMP
from app.models.base import Base

class QueryModel(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True, index=True)
    request = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    datecreated = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
