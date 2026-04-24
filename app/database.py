# This file is going to handle our database connection and other related operations.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL='postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL='postgresql://postgres:root%40123@localhost/fastapi'  # Right now this is a bad practice later we will change it 


# Creating the Engine
Engine=create_engine(SQLALCHEMY_DATABASE_URL)

# Creating the SessionLocal class
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base=declarative_base() # This is the base class for our models. It is used to create the tables in the database. We will use this base class to create our models later.



# Dependency , it refers to the database session
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
