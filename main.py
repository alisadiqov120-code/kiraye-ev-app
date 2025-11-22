from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"status": "ok", "message": "Kiraye ev app working!"}
