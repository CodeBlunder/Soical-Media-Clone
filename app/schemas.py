from pydantic import BaseModel
from datetime import datetime
from pydantic import EmailStr
from typing import Optional

# The below code defines the Pydantic models for the Post entity. These models are used to validate and serialize the data for creating and updating posts in the API.
class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True
    
# Here i have created two seperate models we are just passing the postbase model to both the create and update models because the fields are same for both the operations but if we have different fields for create and update operations then we can define them separately.

class PostCreate(PostBase):
    pass  

# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool=True


# class UpdatePost(BaseModel):
#     title: str
#     content: str
#     published: bool=True



class UserOut(BaseModel):
    id: int
    email: EmailStr
    

    class Config:
        form_attributes=True

# Now will create response model for the post which will be used to serialize the data when we return the response from the API.
class Post(PostBase):
    id: int
                                    # We inherited the PostBase we can reuse the fields and can add additional fields to it according to the requirement
                                    
    created_at: datetime
    user_id: int
    Owner: UserOut
# Even though we are not sending the id and created_at fields , we don't want user to see this fieds
    class Config:
        form_attributes=True  #orm_mode=True  # These two lines are used to tell Pydantic that the data we are going to receive from the database is going to be in the form of an ORM model and we want to convert it into a Pydantic model before returning it as a response. This is necessary because SQLAlchemy returns data in the form of ORM models, and we want to convert it into a format that can be easily serialized and returned as a response in our API. By setting orm_mode to True, we can ensure that the data is properly converted and returned in the expected format.



# Schema for the user entity
class UserCreate(BaseModel):
    
    email: EmailStr
    password: str
    



class UserLogin(BaseModel):
    email: EmailStr
    password: str
    


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int]=None
    

