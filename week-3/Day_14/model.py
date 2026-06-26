from database import Base
from sqlalchemy import Column, Integer,String

class Todo(Base):
    __tablename__ = "todo_list"

    id= Column (Integer,primary_key=True)
    title= Column(String(50), nullable=False)
    description = Column(String(150), nullable=False)

    


