from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# from . import curd,models, schema
from app import curd, models, schema
from .database import sessionLocal, engine

models.Base.metadata.create_all(bind=engine)
# models.Base


app = FastAPI()

#Dependency
def get_db():
    db = sessionLocal()
    try : 
        yield db
    finally:
        db.close()


@app.post("/users/",response_model=schema.User)
def post_user(user:schema.UserCreate, db:Session=Depends(get_db)):
    db_user = curd.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return curd.create_user(db=db,user=user)


@app.get("/users/", response_model=list[schema.User])
def get_users(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    users = curd.get_users(db,skip=skip,limit=limit)
    return users


@app.get("/users/{user_id}/",response_model=schema.User)
def get_user(user_id:int, db:Session=Depends(get_db)):
    db_user = curd.get_user(db,user_id =user_id )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/todos/",response_model=schema.Todo)
def post_todo_for_user(user_id:int, todo:schema.TodoCreate, db:Session=Depends(get_db)):
    return curd.create_user_todo(db=db,user_id=user_id, todo=todo)


@app.get("/todos/", response_model=list[schema.Todo])
def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    todos = curd.get_todos(db,skip=skip,limit=limit)
    return todos