from database import Base
from sqlalchemy import Boolean, Column, Integer, String


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String)
    body = Column(String)
    # published = Column(Boolean)
