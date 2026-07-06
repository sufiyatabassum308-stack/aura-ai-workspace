from fastapi import FastAPI
from app.routers.chat import router as chat_router

app = FastAPI(
    title="AURA AI Workspace",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AURA AI Workspace 🚀"
    }


app.include_router(chat_router)