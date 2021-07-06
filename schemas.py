from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    author: str
    body: str


class User(BaseModel):
    userName: str
    email: str
    password: str


class ShowBlog(Blog):
    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True
