from enum import Enum

#3.10 버전 이상 Union을 안써도 변경 가능 
#https://peps.python.org/pep-0604/
#from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Query Parameter DB
fake_item_db = [
    {"item_name": "foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

@app.get("/") #데코레이션
async def root():
    return {"message": "Hello World"}

'''
### Query Parameter Function

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_item_db[skip : skip + limit]
'''
'''
### Query Parameter Type Conversion
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False): 
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
'''
#여러 경로 / 쿼리 매개 변수
'''
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q })
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
'''

'''
#필수 쿼리 매개변수

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str,
    needy: str
):
    item = {"item_id": item_id, "needy": needy}
    return item
'''
'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if q: #q가 None이 아닐 경우
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id} #q가 None일 경우
'''

#종합쿼리
@app.get("/items/{items_id}")
async def read_user_item(
    item_id: str,
    needy: str,
    skip: int = 0,
    limit: int | None = None
):
    item = {
        "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit
    }
    return item

#PUT Method 사용
'''
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}
'''