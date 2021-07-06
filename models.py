from database import Base
from sqlalchemy import Boolean, Column, Integer, String


# Model (Table) for the Blog
class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String)
    body = Column(String)
    # published = Column(Boolean)


# Model (Table) for the users
class User(Base):
    __tablename__ = "userdata"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
