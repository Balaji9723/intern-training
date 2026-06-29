from sqlalchemy import Column, Integer, String, Text, ForeignKey,create_engine
from sqlalchemy.orm import sessionmaker, declarative_base,relationship

# Base = declarative_base()

DATABASE_URL = "postgresql://postgres:Thasmag97@localhost:5432/postgres"
engine= create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit= False,
    autoflush=False,
    bind= engine)

Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"
    id= Column (Integer,primary_key=True)
    name= Column(String(50), nullable=False)
    age= Column(Integer)
    # one user to many posts
    posts = relationship("Post", back_populates="author")
    def __repr__(self):
        return f"user(id={self.user_id}, name='{self.name}')"


# post mode
class Post(Base):
    __tablename__ = "posts"

    post_id  = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text)
    user_id = Column(Integer,ForeignKey("users.id"))
    # many posts to one user
    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"user(id={self.post_id}, title='{self.title}')"
    
# creates table
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine) 
# create session
session = SessionLocal()

# Create
new_user =User (id= 101, name = "Balaji", age= 28 )

session.add(new_user)
session.commit()
print("user created successfully")

new_post= Post (
    post_id =1,
    title= "java",
    content= "wwww",
    user_id= 101    
)
session.add(new_post)
session.commit()
print("post created successfully")

# Read
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age )
print("\nUser Posts")
user = session.query(User).filter_by(name="Balaji").first()
if user:
    for post in user.posts:
        print(post.post_id, post.title)

# Update
user = session.query(User).filter_by(name="Balaji").first()
if user:
    user.name = "bala"
    user.age = 25
    session.commit()
    print("User updated successfully")
# update post    
post = session.query(Post).first()
if post:
    post.title = "Advanced FastAPI"
    session.commit()

    print("Post updated successfully")

# READ AFTER UPDATE
users = session.query(User).all()

for user in users:
    print(user)

posts = session.query(Post).all()

for post in posts:
    print(post)


# Delete post
post = session.query(Post).first()
session.delete(post)
session.commit()

print("Post deleted successfully")

# Delete user

user = session.query(User).filter_by(name="Bala").first()
if user:
    session.delete(user)
    session.commit()
    print("User deleted successfully")

# Close session
session.close()

print("\nSession closed")

