from typing import List
from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from controllers import user

import models
import schemas
from database import get_db

router = APIRouter()


@router.get('/users', response_model=List[schemas.ShowUser], tags=["Users"])
def get_users(db: Session = Depends(get_db)):
    return user.read(db)


@router.get('/users/{id}', response_model=schemas.ShowUser, tags=["Users"])
def get_user(id: int, db: Session = Depends(get_db)):
    return user.read_one(id, db)


@router.post('/users', response_model=schemas.ShowUser, tags=["Users"])
def create_user(users: schemas.User, db: Session = Depends(get_db)):
    return user.create(users, db)


@router.delete('/user/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["Users"])
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.delete(id, db)
