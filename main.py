from fastapi import FastAPI

app = FastAPI()

@app.get("/sample/test")
def first():
    return {"Welcome sample apis"}



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

users_db = {}

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@app.post("/register")
def register(user: RegisterRequest):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already registered")

    users_db[user.email] = {
        "email": user.email,
        "password": user.password,
    }

    return {
        "message": "Registration successful",
        "user": {
            "email": user.email,
            "password": user.password,
        },
    }


@app.post("/login")
def login(user: LoginRequest):
    stored_user = users_db.get(user.email)

    if not stored_user:
        raise HTTPException(status_code=404, detail="User not found")

    if stored_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {
        "message": "Login successful",
        "user": {
            "email": stored_user["email"],
            "password": stored_user["password"],
        },
    }