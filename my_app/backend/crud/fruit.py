from backend.models.fruit import Fruit
from fastapi import HTTPException

def add_fruit(db, fruit):
    db_fruit = Fruit(**fruit.dict()) #Pydantic model to SQLAlchemy model (ORM)
    db.add(db_fruit)
    db.commit()
    db.refresh(db_fruit)
    return db_fruit

def get_fruit(db, fruit_id):
    fruit = db.query(Fruit).filter(Fruit.id == fruit_id).first()
    if fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return fruit

def get_fruits(db):
    fruits = db.query(Fruit).all()
    return fruits