from fastapi import FastAPI, Depends, status, Response, HTTPException
import models
from database import engine, SessionLocal
import schemas
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Read All the blogs
@app.get('/blogs', status_code=status.HTTP_200_OK)
def read_blogs(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    if blogs:
        response.status_code = status.HTTP_200_OK
        return blogs
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


# Read a particular blog with particular id
@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
    else:
        return blogs


# Post a blog to the database
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def post_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, author=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Delete a blog from the database
@app.delete('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Deleted Successfully"}


# Updating a pre-existing blog
@app.put('/blog/{id}')
def update_blog(id: int, blog: schemas.Blog, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"Blog with id {id} is not found")
    blogs.update(vars(blog))
    # vars is used to convert an object into dict
    db.commit()
    return {"message": "Updated Successfully"}
