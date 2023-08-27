from typing import Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import SessionLocal
from models import Item

app=FastAPI()

class ItemSerializer(BaseModel):
    id:int
    name:str
    on_offer:bool
    price:float
    description:str
    
    class Config:
        orm_mode = True
        
db = SessionLocal()
@app.get('/items', response_model=List[ItemSerializer], status_code=200)
def list_items():
    items = db.query(Item).all()
    return items

@app.get("/items/{id}")
def retrieve_item(id:int, response_model=ItemSerializer, status=200):
    item = db.query(Item).filter(Item.id==id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item with this ID does not exist")
    return item

@app.post("/items", response_model=ItemSerializer, status_code=201)
def create_item(item:ItemSerializer):
    data = item.model_dump(mode='json')
    name_exists:bool = db.query(db.query(Item).filter(Item.name==data.get("name")).exists()).scalar()
    if name_exists:
        raise HTTPException(status_code=409,  detail="Item with this name already exist")
    new_item = Item(**data)
    db.add(new_item)
    db.commit()
    return new_item

@app.put("/items/{id}",  response_model=ItemSerializer, status_code=200)
def update_item(id:int, item:ItemSerializer):
    db_item = db.query(Item).filter(Item.id==id).first()
    if not db_item:
        raise  HTTPException(status_code=404,  detail="Item with this ID does not exist")
    data = item.model_dump(mode='json')
    for key, value in data.items():
        setattr(db_item, key, value)
    db.commit()
    return db_item

@app.delete("/items/{id}", status_code=200)
def delete_item(id:int):
    db_item = db.query(Item).filter(Item.id==id).first()
    if not db_item:
        raise  HTTPException(status_code=404,  detail="Item with this ID does not exist")
    db.delete(db_item)
    return db_item