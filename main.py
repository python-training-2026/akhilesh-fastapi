from fastapi import FastAPI

app = FastAPI()

@app.get("/sample/test")
def first():
    return {"Welcome sample apis"}

