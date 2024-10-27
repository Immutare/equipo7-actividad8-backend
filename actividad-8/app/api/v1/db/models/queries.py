from sqlalchemy import Column, Integer, Text, TIMESTAMP
from app.api.v1.db.base import Base

class QueryModel(Base):
    __tablename__ = "queries"

    idqueries = Column(Integer, primary_key=True, index=True)
    naturallanguagerequest = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    timeofrequest = Column(TIMESTAMP, nullable=False)
