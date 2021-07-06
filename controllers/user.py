from fastapi import Depends, status, Response, HTTPException, APIRouter
import models
from sqlalchemy.orm import Session
from passlib.context import CryptContext


def read(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users Exists")
    else:
        return users


def read_one(id, db: Session):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User is not registered, kindly register first")
    else:
        return users


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create(user, db: Session):
    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(name=user.userName, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete(id, db: Session):
    users = db.query(models.User).filter(models.User.id == id)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    users.delete(synchronize_session=False)
    db.commit()
    return {"message": "Deleted Successfully"}
