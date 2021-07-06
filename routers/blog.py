from typing import List
from fastapi import Depends, status, Response, HTTPException, APIRouter
from database import get_db
from sqlalchemy.orm import Session
import schemas
from controllers import blog

router = APIRouter()


@router.get('/blogs', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog], tags=["Blogs"])
def read_blogs(response: Response, db: Session = Depends(get_db)):
    return blog.read(db, response)


# Read a particular blog with particular id
@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=["Blogs"])
def get_blog(id: int, response: Response, db: Session = Depends(get_db)):
    return blog.read_one(id, db)


# Post a blog to the database
@router.post('/blog', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog, tags=["Blogs"])
def post_blog(blogs: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(blogs, db)


# Delete a blog from the database
@router.delete('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)


# Updating a pre-existing blog
@router.put('/blog/{id}', tags=["Blogs"])
def update_blog(id: int, blogs: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, blogs, db)
