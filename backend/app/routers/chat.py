from fastapi import APIRouter

from app.schemas.chat_schema import ChatRequest
from app.services.gemini_service import generate_response

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    answer = generate_response(request.question)

    return {
        "question": request.question,
        "response": answer
    }