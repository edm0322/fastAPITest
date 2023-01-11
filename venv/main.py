from fastapi import FastAPI, Query

app = FastAPI()

'''
@app.get("/items/")
async def read_items(q: str | None = None):
    results = {
        "items":[
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ]
    }
    if q:
        results.update({"q": q})
    return results
'''

# Parameter Value Validation
# import Query를 해야한다.
'''
@app.get("/items/")
async def read_items(q: str| None = Query(default=None, max_length=50, min_length=3)):
    result= {
        "items" : [
            {"item_id": "Foo"},
            {"item_id": "bar"}
        ]
    }
    if q:
        result.update({"q": q})
    return result
'''

'''
#Parameter Value Validation With Regex

@app.get("/items/")
async def read_items(
    q: str | None = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {
        "items":[
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ]
    }
    if q:
        results.update({"q":q})
    return results
'''
'''
#Defalut Value
@app.get("/items/")
async def read_items(q: str = Query(defalut="fixedquery", min_length=3)):
    results = {
        "items" : [
            {"item_id": "Foo"},
            {"item_id": "bar"}
        ]
    }
    if q:
        results.update({"q": q})
    return results
'''

'''
#Using Ellipsis
@app.get("/items/")
async def read_items(q: str = Query(default=..., min_length=3)):
    results = {
        "items":[
            {"items_id", "foo"},
            {"items_id", "bar"}
        ]
    }
    if q:
        results.update({"q": q})
    return results
'''

'''
# Using Ellipsis with None
@app.get("/items/")
async def read_items(q: str | None = Query(default=..., min_length=3)):
    results = {
        "items": [
            {"item_id":"foo"},
            {"item_id":"bar"}
        ]
    }
    if q:
        results.update({"q":q})
    return results
'''

'''
# Using PYdantic Required
from pydantic import Required

@app.get("/items/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [
            {"item_id": "foo"},
            {"item_id": "bar"}
        ]
    }
    if q:
        results.update({"q" : q})
    return results
'''

'''
# Query List / Multiple Value
@app.get("/items/")
async def read_items(q: list[str] | None = Query(default=None)):
    query_items = {"q": q}
    return query_items
'''


# Query List / Multiple Value Defaults
'''
@app.get("/items/")
#async def read_items(q: list[str] = Query(default=['foo', 'bar'])):
## List Default
async def read_item(q: list = Query(default=[])):
    query_items = {"q":q}
    return query_items

'''


