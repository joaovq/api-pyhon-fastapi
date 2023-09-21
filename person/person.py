from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from core.utils.app import create_app
from database import  get_db
from repositories import person_repository
import schemas
from fastapi import status
from fastapi.responses import JSONResponse

person = create_app()

@person.post("/person/")
async def create_person(person: schemas.PersonCreate,db: Session = Depends(get_db)):
    if person.age < 0:
        raise HTTPException(status_code=400, detail="Age should be > 0")
    
    return JSONResponse(status_code=status.HTTP_201_CREATED,content=person_repository.create_person(db, person))

@person.post("/person/{person_id}/sales/")
async def create_person_sales(sale: schemas.SalesCreate,person_id: int,db: Session = Depends(get_db)):
    if sale.value < 0:
        raise HTTPException(status_code=400, detail="Value should be > 0")
    return person_repository.create_sale_person(db,sale, person_id)

@person.get("/person/{id}")
async def get_person(id: int, db: Session = Depends(get_db)):
    return person_repository.get_person_by_id(db, id)

@person.get("/person/")
async def get_persons(db: Session = Depends(get_db)):
    return person_repository.get_persons(db)

@person.get('/person/sales/')
def get_sales(db: Session = Depends(get_db)):
    return person_repository.get_all_sales(db)

@person.get('/person/{person_id}/sales/')
def get_sales(person_id: int,db: Session = Depends(get_db)):
    return person_repository.get_person_sales(db, person_id)