import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a supported model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(question, context_chunks):
    context = "\n\n".join(
    [f"[{c['source']}]\n{c['text']}" for c in context_chunks]
)

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the information provided in the context.

Rules:
1. Answer using only the context.
2. If the user asks for a summary, summarize the context.
3. If the user asks for important points, list the important points from the context.
4. If the answer is not clearly present in the context, say:
   "I could not find this in the document."
    Do not guess.

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)
    return response.text