from enum import Enum

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Query Parameter DB
fake_item_db = [
    {"item_name": "foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None #Default 지정자

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.vale == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/") #데코레이션
async def root():
    return {"message": "Hello World"}

'''
### Query Parameter Function

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_item_db[skip : skip + limit]
'''

### Query Parameter Type Conversion
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if q: #q가 None이 아닐 경우
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id} #q가 None일 경우
'''

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}