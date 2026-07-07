import os
from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import split_text_into_chunks
from app.services.embedding_service import get_embeddings
from app.services.vector_store import add_to_vector_store, search
from app.services.gemini_service import generate_response
from app.services.memory_service import add_message, get_history

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)




@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # save file
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # extract text
    text = extract_text_from_pdf(file_path)

    # split into chunks
    chunks = split_text_into_chunks(text)

    # embeddings
    embeddings = get_embeddings(chunks)

    # store in vector DB
    add_to_vector_store(chunks, embeddings)

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "message": "PDF processed and stored successfully"
    }


@router.post("/ask-pdf")
async def ask_pdf(question: str):

    try:
        print("QUESTION:", question)
        add_message("User", question)

        query_embedding = get_embeddings([question])[0]
        print("EMBEDDING DONE")

        results = search(query_embedding, top_k=8)
        print("SEARCH DONE:", results)

        answer = generate_response(question, results)

        add_message("AURA", answer)
        print("GEMINI DONE")

        return {
            "question": question,
            "answer": answer,
            "sources": results
        }

    except Exception as e:
        print("ERROR OCCURRED:", str(e))
        return {
            "error": str(e)
        }
    