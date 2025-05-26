from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.fruit import FruitIn, FruitOut
from backend.crud.fruit import get_fruits, get_fruit, add_fruit
from backend.core.db import get_session
from typing import List

router = APIRouter()

@router.get("/fruit", response_model=List[FruitOut])
def get_fruits_route(db = Depends(get_session)):
    return get_fruits(db)

@router.get("/fruit/{fruit_id}", response_model=FruitOut)
def get_fruits_route(fruit_id: int, db = Depends(get_session)):
    return get_fruit(db, fruit_id)

@router.post("/fruit", response_model=FruitOut)
def add_fruit_route(fruit: FruitIn, db = Depends(get_session)):
    db_fruit = add_fruit(db, fruit)
    if db_fruit is None:
        raise HTTPException(status_code=400, detail="Fruit already exists")
    return db_fruit
