# Day- 9

from fastapi import FastAPI
app= FastAPI()

list = []

@app.get("/")
def welcome():
    return {"msg":"Welcome to FastAPI"}

@app.get("/hello/{name}")
def hello(name):
    return {"msg":f"Hello {name}"}

@app.post("/create")
def create(item):
    list.append(item)
    return {"msg":"Iteam added successfully"}

@app.put("/put")
def update(id,update_item):
    list[int(id)-1] = update_item
    return {"msg":"Item Updated successfully"}

@app.get("/read")
def show():
    return list
