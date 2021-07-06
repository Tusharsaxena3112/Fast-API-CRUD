from typing import List

from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    author: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    userName: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]

    class Config:
        orm_mode = True


class ShowBlog(Blog):
    creator: ShowUser

    class Config:
        orm_mode = True
