# Correct code..
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import get_db ,Base ,engine
from sqlalchemy.orm import Session 
from model import Todo

application = FastAPI()

class Task(BaseModel):
    title: str
    description:str

@application.get("/")
def read_task(db:Session = Depends(get_db)):
    return db.query(Todo).all()

@application.get("/{id}")
def read_task(id:int,db:Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id==id).first()
    if task is None:
        raise HTTPException(status_code=404,detail="Id is incorrect")
    return task


@application.post("/task")
def set_task(task:Task, db:Session =Depends(get_db)):
    # res = db.query(Todo).filter(id=task.id).first()
    # if res != None:
    #     return {"msg": "task already found"}
    new_task = Todo( title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    return {"msg": "task added successfully"}

@application.put("/put/{id}")
def update_task(id:int, task: Task,  db:Session= Depends(get_db)):
    result = db.query(Todo).filter(Todo.id==id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Id is incorrect")
    result.title = task.title
    result.description =task.description
    db.commit()
    return{"msg": "Updated successfully"}

@application.delete("/delete/{id}")
def delete(id:int, db:Session = Depends(get_db)):
    result =db.query(Todo).filter(Todo.id==id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Id is incorrect")
    db.delete(result)
    db.commit()
    return{"msg":"deleted successfully"} 




# from fastapi import FastAPI, HTTPException, Depends
# from pydantic import BaseModel
# from database import get_db ,Base ,engine
# from sqlalchemy.orm import Session 
# from model import Todo

# Base.metadata.create_all(bind=engine)

# application = FastAPI()
# class RegisterTasks(BaseModel):
#     emp_id: int
#     emp_name: str
#     emp_email: str
#     emp_age: int


# @application.get("/")
# def read_msg(db:Session = Depends(get_db)):
#     return db.query(Todo).all()

# @application.get("/{id}")
# def read_msg(id:int,db:Session = Depends(get_db)):
#     task = db.query(Todo).filter(Todo.id==id).first()
#     if task is None:
#         raise HTTPException(status_code=404,detail="Id is incorrect")
#     return task


# @application.post("/emptask")
# def register(emp_data:RegisterTasks,db:Session=Depends(get_db)): 
#         reg = db.query(Todo).filter(Todo.id==emp_data.emp_id).first()
#         if reg:
#              return {"msg":"user already found"}
        
#         user= Todo(id=emp_data.emp_id,title=emp_data.emp_name,description=emp_data.emp_name)
#         db.add(user)
#         db.commit()
#         return {"msg": "success"}
    

# @application.put("/put/{id}")
# def update(id: int, emp_data: RegisterTasks, db:Session=Depends(get_db)):
#     task = db.query(Todo).filter(Todo.id==id).first()
#     if task is None:
#         raise HTTPException(status_code=404, detail="Id is incorrect")
#     task.title = emp_data.title

# @application.delete("/delete/{id}")
# def delete(id:int):
#     if(len(l) > id): 
#         del l[id]
#         return {"message":"delete successfully"}
#     raise HTTPException(status_code=404,detail="Id is incorrect")