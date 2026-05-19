from fastapi import FastAPI
from database.db import engine, Base  #Database connection engine, Parent class for all models
from routers.auth import router as auth_router #Import router from auth file

app = FastAPI()

app.include_router(auth_router) #Add auth routes into FastAPI app.

@app.on_event("startup") #Run function automatically when server starts.
async def startup(): #Async startup function.

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) #Create all tables automatically.

@app.get("/")
async def home():
    return {"message": "FastAPI PostgreSQL Project"}