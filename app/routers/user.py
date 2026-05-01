from .. import models, schemas , utils # .. refers to the parent directory , it means we are referring the above directory from the current directory i.e parent directory
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from .. utils import hash_pass

router=APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):
    # Before creating a new user, we need to hash the password. we will be using password_hash to hash the password
    hashed_pass=hash_pass(user.password)
    user.password=hashed_pass

    
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user 






@router.get("/{id}",response_model=schemas.UserOut)  
def get_user(id: int, db:Session=Depends(get_db)):   
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} was not found")
    return user
