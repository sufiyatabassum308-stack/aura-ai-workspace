from fastapi import APIRouter, UploadFile, File
import os

from app.schemas.chat_schema import ChatRequest
from app.services.gemini_service import generate_response
from app.services.document_service import DOCUMENT_STORE, extract_text_from_pdf


router = APIRouter()