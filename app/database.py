# This file is going to handle our database connection and other related operations.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings
    
# SQLALCHEMY_DATABASE_URL='postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
# SQLALCHEMY_DATABASE_URL='postgresql://postgres:root%40123@localhost/fastapi'  # Right now this is a bad practice later we will change it 

SQLALCHEMY_DATABASE_URL=f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'  

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



"""
while True:
    try:
        conn= psycopg2.connect(host='localhost', database='fastapi', user='postgres',password='root@123',cursor_factory=RealDictCursor) # Cursor factory is used to specify the type of cursor that we want to use. In this case, we are using RealDictCursor which returns the query results as a list of dictionaries instead of tuples. This allows us to access the data using column names instead of index positions.
        cursor=conn.cursor()
        print("Database connection was successful")
        break
    except Exception as e:
        print("Database connection failed")
        print('Error:', e)
        time.sleep(2) # This is used to wait for 2 seconds before trying to connect to db
"""