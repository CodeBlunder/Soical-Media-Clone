# This file is going to handle our database connection and other related operations.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL='postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL='postgresql://postgres:root@123@localhost/fastapi'  # Right now this is a bad practice later we will change it 


# Creating the Engine
Engine=create_engine(SQLALCHEMY_DATABASE_URL)

# Creating the SessionLocal class
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base=declarative_base() # This is the base class for our models. It is used to create the tables in the database. We will use this base class to create our models later.


models.Base.metadata.create_all(bind=Engine) # This is used to create the tables in the database. It will create all the tables that are defined in the models.py file. We will use this line of code to create the tables in the database when we run the application for the first time. After that, we can comment it out or remove it from the code.