from sqlalchemy.orm import Session
from app.models.queries import QueryModel
from app.api.routes.queries.queries_dto import QueryCreate

def get_query(db: Session, query_id: int):
    return db.query(QueryModel).filter(QueryModel.idqueries == query_id).first()

def create_query(db: Session, query: QueryCreate):
    db_query = QueryModel(**query.dict())
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

def get_queries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(QueryModel).offset(skip).limit(limit).all()

def delete_query(db: Session, query_id: int):
    db_query = db.query(QueryModel).filter(QueryModel.idqueries == query_id).first()
    if db_query:
        db.delete(db_query)
        db.commit()
        return db_query
    return None
