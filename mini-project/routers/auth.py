from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_db  ##Import database session function,This function gives DB connection to API.
from models.user import User #Import User model, Used to insert data into PostgreSQL table.
from schemas.user import UserRegister #Import Pydantic schema, Used for request validation

router = APIRouter()

@router.post("/register")
async def register( #Create async function for register API.
    user: UserRegister, #Receive request body data.

    # Get database session automatically.
    # Depends(get_db) → Call get_db()
    # Create DB connection
    # Pass session into API
    db: AsyncSession = Depends(get_db)
):

    new_user = User( #Create new User object.
        name=user.name, #Take name from request body.
        email=user.email,
        password=user.password
    )

    db.add(new_user) #Add user object into database session.  Data is not saved yet.

    await db.commit() #Save data permanently into PostgreSQL.

    return {
        "message": "User Registered"
    }

