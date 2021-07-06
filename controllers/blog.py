from fastapi import Depends, status, Response, HTTPException, APIRouter
import models
from sqlalchemy.orm import Session


def read(db: Session, response: Response):
    blogs = db.query(models.Blog).all()
    if blogs:
        response.status_code = status.HTTP_200_OK
        return blogs
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


def read_one(id, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
    else:
        return blogs


def create(blog, db: Session):
    new_blog = models.Blog(title=blog.title, author=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Deleted Successfully"}


def update(id: int, blog, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    blogs.update(vars(blog))
    # vars is used to convert an object into dict
    db.commit()
    return {"message": "Updated Successfully"}
