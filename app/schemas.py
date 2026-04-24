from pydantic import BaseModel

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


