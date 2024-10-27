from sqlalchemy.orm import Session
from app.models.queries import QueryModel
from app.api.routes.queries.queries_dto import QueryCreate, QueryUpdate

def get_query(db: Session, query_id: int):
    return db.query(QueryModel).filter(QueryModel.id == query_id).first()

def create_query(db: Session, query: QueryCreate):
    db_query = QueryModel(**query.dict())
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

def update_query(db: Session, query_id: int, query: QueryUpdate):
    db_query = db.query(QueryModel).filter(QueryModel.id == query_id).first()
    db.add(db_query)

    db_query.request = query.request or db_query.request
    db_query.response = query.response or db_query.response
    db_query.datecreated = query.datecreated or db_query.datecreated

    db.commit()
    db.refresh(db_query)
    return db_query

def get_queries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(QueryModel).offset(skip).limit(limit).all()

def delete_query(db: Session, query_id: int):
    db_query = db.query(QueryModel).filter(QueryModel.id == query_id).first()
    if db_query:
        db.delete(db_query)
        db.commit()
        return db_query
    return None
