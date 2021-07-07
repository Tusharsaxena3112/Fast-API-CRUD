from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

import models
import schemas
import database

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/login', tags=["Authentication"])
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(request.username == models.User.name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exists, register first")
    if not pwd_context.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Password")
    return request
