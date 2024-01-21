# type "uvicorn working:app --reload" in terminal
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}


@app.get('/get-item/{item_id}')
def get_item(item_id:int = Path(..., description='id you look', gt=0)):
    return inventory[item_id]

@app.get('/get-by-name/{item_id}')   #get-by-name?name=milk
def get_item(name:str = Query(..., title='name', description='name of item')):   #set name parameter is optional 
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail='item name not found.')

@app.post('/create-item/{item_id}')
def create_item(item_id:int, item:Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail='id already exist.')
    
    inventory[item_id] = item
    return inventory[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id:int, item=UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail='id does not exist.')
    
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@app.delete('/delete-item/{item_id}')
def delete_item(item_id:int = Query(..., description='id to delete', gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail='id does not exist.')
    
    del inventory[item_id]
    return {'success':'item deleted'}