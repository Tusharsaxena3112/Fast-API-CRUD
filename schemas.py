from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    author: str
    body: str


class ShowBlog(Blog):
    class Config():
        orm_mode = True
