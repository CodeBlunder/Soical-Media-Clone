from fastapi import APIRouter, Depends,HTTPException, status, Response
from sqlalchemy.orm import Session
from .. import database,schemas , models , utils

router=APIRouter(
    tags=['Authentication']

)

@router.post("/login")
def login(user_credentials:schemas.UserLogin,db:Session=Depends(database.get_db)):
    user =db.query(models.User).filter(models.User.email==user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utils.verify_pass(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

   
    
    # Create a token and return it to the user

    return {"token":"dummy token"}
