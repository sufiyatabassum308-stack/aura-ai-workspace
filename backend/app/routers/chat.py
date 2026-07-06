from fastapi import APIRouter

router = APIRouter()


@router.post("/chat")
def chat():

    return {
        "response": "Hello! I am AURA AI 🚀"
    }