
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

Person = list([
    Person(id=1, name="Alex", age=25),
    Person(id=2, name="Felix", age=30),
    Person(id=3, name="Max", age=35)

])

@app.get("/api")
def read_root():
    return Person


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}