from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

application = FastAPI()

class RegisterTasks(BaseModel):
    emp_id: int
    emp_name: str
    emp_email: str
    emp_age: int

l = []


@application.get("/")
def read_msg():
    return l

@application.get("/{id}")
def read_msg(id:int):
    if(len(l) > id): return l[id]
    raise HTTPException(status_code=404,detail="Id is incorrect")


@application.post("/emptask")
def register(emp_data:RegisterTasks): 
        l.append(emp_data)
        return {"message": "registered sucessfully"}
    

@application.put("/put/{id}")
def update(id: int, emp_data: RegisterTasks):
    if len(l) > id:
        l[id] = emp_data
        return {"message": "Updated successfully"}

    raise HTTPException(status_code=404, detail="Id is incorrect")

@application.delete("/delete/{id}")
def delete(id:int):
    if(len(l) > id): 
        del l[id]
        return {"message":"delete successfully"}
    raise HTTPException(status_code=404,detail="Id is incorrect")