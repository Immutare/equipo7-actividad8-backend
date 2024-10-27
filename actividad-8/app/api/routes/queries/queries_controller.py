from fastapi import APIRouter, Depends, HTTPException,Body
from sqlalchemy.orm import Session
from app.services import queries_service as crud
from app.api.routes.queries import queries_dto as dtos
from app.db.session import get_db
from typing import List
 
router = APIRouter()



@router.get("/{query_id}", response_model=dtos.Query)
def read_query(query_id: int, db: Session = Depends(get_db)):
    db_query = crud.get_query(db, query_id=query_id)
    if db_query is None:
        raise HTTPException(status_code=404, detail="Query not found")
    return db_query

@router.get("/", response_model=List[dtos.Query])
def read_queries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_queries(db, skip=skip, limit=limit)

@router.post("/", response_model=dtos.Query)
def create_query(query: dtos.QueryCreate = Body(...), db: Session = Depends(get_db)):
    return crud.create_query(db=db, query=query)


@router.patch("/{query_id}", response_model=dtos.Query)
def update(query_id: int, query: dtos.QueryUpdate = Body(...), db: Session = Depends(get_db)):
    return crud.update_query(db=db, query_id=query_id, query=query)

@router.delete("/{query_id}", response_model=dtos.Query)
def delete_query(query_id: int, db: Session = Depends(get_db)):
    db_query = crud.delete_query(db, query_id=query_id)
    if db_query is None:
        raise HTTPException(status_code=404, detail="Query not found")
    return db_query
