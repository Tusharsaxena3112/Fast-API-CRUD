from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey


# Model (Table) for the Blog
class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String)
    body = Column(String)
    # published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("userdata.id"))

    creator = relationship("User", back_populates='blogs')


# Model (Table) for the users
class User(Base):
    __tablename__ = "userdata"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")
