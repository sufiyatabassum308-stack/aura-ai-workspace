from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    return {
        "question": request.question,
        "response": "Hello! I am AURA AI 🚀"
    }