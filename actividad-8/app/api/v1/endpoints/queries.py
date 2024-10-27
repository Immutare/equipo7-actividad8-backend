from fastapi import APIRouter, Depends, HTTPException,Body
from sqlalchemy.orm import Session
#from app.api.v1 import crud
from app.api.v1.crud import queries as crud
from app.api.v1.schemas import queries as schemas
from app.api.v1.db.session import get_db
from typing import List
 
router = APIRouter()

@router.post("/", response_model=schemas.Query)
def create_query(query: schemas.QueryCreate = Body(...), db: Session = Depends(get_db)):
    return crud.create_query(db=db, query=query)

@router.get("/{query_id}", response_model=schemas.Query)
def read_query(query_id: int, db: Session = Depends(get_db)):
    db_query = crud.get_query(db, query_id=query_id)
    if db_query is None:
        raise HTTPException(status_code=404, detail="Query not found")
    return db_query

@router.get("/", response_model=List[schemas.Query])
def read_queries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_queries(db, skip=skip, limit=limit)

@router.delete("/{query_id}", response_model=schemas.Query)
def delete_query(query_id: int, db: Session = Depends(get_db)):
    db_query = crud.delete_query(db, query_id=query_id)
    if db_query is None:
        raise HTTPException(status_code=404, detail="Query not found")
    return db_query
