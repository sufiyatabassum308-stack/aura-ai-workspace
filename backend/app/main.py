from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers import document, chat  # include both routers if you have them

app = FastAPI(title="AURA AI Workspace")

# -----------------------------
# CORS (IMPORTANT for frontend)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Include routers
# -----------------------------
app.include_router(document.router)
app.include_router(chat.router)

# -----------------------------
# Serve static frontend (UI)
# -----------------------------
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "AURA AI Backend is running",
        "ui": "Open /static/index.html"
    }