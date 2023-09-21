from sqlalchemy.orm import Session
import schemas, models


def create_person(db: Session,person: schemas.PersonCreate):
    person_created = models.Person(name=person.name, age=person.age, email=person.email)
    db.add(person_created)
    db.commit()
    db.refresh(person_created)
    return person_created

def get_person_by_id(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()

def get_all_sales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sale).offset(skip).limit(limit).all()

def get_person_sales(db: Session,person_id: int):
    return list(db.query(models.Sale).filter(models.Sale.person_id == person_id))

def get_persons(db: Session):
    return db.query(models.Person).all()

def create_sale_person(db: Session, sales: schemas.SalesCreate, person_id: int):
    sale_create = models.Sale(**sales.model_dump(), person_id = person_id)
    db.add(sale_create)
    db.commit()
    db.refresh(sale_create)
    return sale_create