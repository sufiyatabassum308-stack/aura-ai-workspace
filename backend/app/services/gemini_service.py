import os

from dotenv import load_dotenv
import google.generativeai as genai

from app.services.memory_service import add_message, get_history

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(question: str):

    # Save the user's question
    add_message("User", question)

    # Get the full conversation
    history = get_history()

    # Send the conversation to Gemini
    response = model.generate_content(history)

    answer = response.text

    # Save Gemini's response
    add_message("Assistant", answer)

    return answer