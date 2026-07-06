chat_history = []


def add_message(role: str, message: str):
    chat_history.append({
        "role": role,
        "message": message
    })


def get_history():

    conversation = ""

    for chat in chat_history:
        conversation += f"{chat['role']}: {chat['message']}\n"

    return conversation


def clear_history():
    chat_history.clear()