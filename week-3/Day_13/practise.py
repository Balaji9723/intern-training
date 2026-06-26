# from sqlalchemy import Column, Integer, String, Text
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base

# class User(Base):

#     __tablename__ = "users"
#     id= Column (Integer,primary_key=True)
#     name= Column(String(50), nullable=False)
#     age= Column(Integer)

# class Post(Base):
#      __tablename__ = "posts"
#     post_id  = Column(Integer, primary_key=True)
#     title = Column(String(100), nullable=False)
#     content = Column(Text)
#     user_id = Column(Integer,ForeignKey("users.user_id"))





# post table...
# create table posts(
# post_id serial primary key,
# title varchar(100) not null,
# content text,
# user_id int,
# foreign key (user_id) references users(id) );

# users table...
# create table users(
# id int, 
# name varchar(50),
# age int);


# correct code
from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Database Connection
DATABASE_URL = "postgresql://postgres:Thasmag97@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)

    # One User -> Many Posts
    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"


# Post Model
class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text)

    user_id = Column(Integer, ForeignKey("users.id"))

    # Many Posts -> One User
    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"Post(post_id={self.post_id}, title='{self.title}')"


# Create Tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create Session
session = SessionLocal()

# ======================
# CREATE
# ======================

new_user = User(
    id=101,
    name="Balaji",
    age=28
)

session.add(new_user)
session.commit()

print("User created successfully")

new_post = Post(
    post_id=1,
    title="Java Basics",
    content="Introduction to Java",
    user_id=101
)

session.add(new_post)
session.commit()

print("Post created successfully")


# ======================
# READ
# ======================

print("\nAll Users")

users = session.query(User).all()

for user in users:
    print(user.id, user.name, user.age)

print("\nUser Posts")

user = session.query(User).filter_by(name="Balaji").first()

if user:
    for post in user.posts:
        print(post.post_id, post.title)


# ======================
# UPDATE USER
# ======================

user = session.query(User).filter_by(name="Balaji").first()

if user:
    user.name = "Bala"
    user.age = 25
    session.commit()

    print("\nUser updated successfully")


# ======================
# UPDATE POST
# ======================

post = session.query(Post).first()

if post:
    post.title = "Advanced FastAPI"
    session.commit()

    print("Post updated successfully")


# ======================
# READ AFTER UPDATE
# ======================

print("\nUpdated Data")

users = session.query(User).all()

for user in users:
    print(user)

posts = session.query(Post).all()

for post in posts:
    print(post)


# ======================
# DELETE POST
# ======================

post = session.query(Post).first()

if post:
    session.delete(post)
    session.commit()

    print("\nPost deleted successfully")


# ======================
# DELETE USER
# ======================

user = session.query(User).filter_by(name="Bala").first()

if user:
    session.delete(user)
    session.commit()

    print("User deleted successfully")


# ======================
# CLOSE SESSION
# ======================

session.close()

print("\nSession closed")