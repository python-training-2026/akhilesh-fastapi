from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession 
#Import async database connection tools.
# create_async_engine → Connect to PostgreSQL
# AsyncSession → Used to perform DB operations

from sqlalchemy.orm import sessionmaker, declarative_base
# sessionmaker → Create DB sessions
# declarative_base → Base class for models

import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB")

#Create PostgreSQL connection URL.
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Create database engine.
# Main connection object
#echo=True → Show SQL queries in terminal

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# FastAPI needs a database session.
# SessionLocal() creates that session.
#SessionLocal → Creates temporary DB connections for APIs

SessionLocal = sessionmaker(
    bind=engine, #Attach session with PostgreSQL engine.
    class_=AsyncSession, #Use async database session.
    expire_on_commit=False #Keep object data after saving.
)

Base = declarative_base() #Create base class for all database models.

async def get_db(): #Create function to provide DB session. Now API can use database operations.
    async with SessionLocal() as session:
        yield session

# Create new database session.

# When API starts:

# Open DB connection

# When API ends:

# Automatically close DB connection