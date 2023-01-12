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

'''
#Declare More metadata
@app.get("/items/")
async def read_items(
    q: str | None = Query(
        default=None,
        title="Query String",
        description="Query string for the items to search in the database that have a good match",
        min_length=3)):
    results = {
        "items": [
            {"items_id":"Foo"},
            {"item_id":"Bar"}
        ]
    }
    if q:
        results.update({"q": q })
    return results

'''

'''
#Alias Parameters
@app.get("/items/")
async def read_items(
    q: str | None = Query(default=None, alias="item-query") #URL에서 표현하기 힘든것들을 여기에서 표현할수 있음.
):
    results = {
        "items": [
            {"item_id" : "foo"},
            {"item_id" : "bar"}
        ]
    }
    if q:
        results.update({"q" : q})
    return results

'''

'''
#Deprecating Parameter
@app.get("/items/")
async def read_items(
    q : str |
    None = Query (
        default = None,
        alias = "item-query",
        title = "Query String",
        description = "Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True
    )
):
    results = {
        "items" : [
            {"item_id":"Foo"},
            {"item_id":"bar"}
        ]
    }
    if q:
        results.update({"q" : q})
    return results
'''

#Exclude from OpenAPI (Automated Docs.)
#OpenAPI에 안잡힌다
@app.get("/items/")
async def read_item(
    hidden_query : str | None = Query(default=None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query" : hidden_query}
    else:
        return {"hidden_query" : "not found"}