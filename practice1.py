

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

user_list=[]

class User(BaseModel) :
    id:str
    name:str

@app.post("/adduser")
def addUser(user:User):
    for item in user_list:
        if item.id == user.id:
          return{"message":"alrady exist user"}
        #  print("alrady exist user")
    user_list.append(user)
    return {"message": "User created", "user":user}



@app.get("/userlist")
def listuser():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):  
    return {"item_id": item_id, "q": q}

@app.post("/employee")
def employee():
    return {"Hello": "World"}

print(user_list,"list")