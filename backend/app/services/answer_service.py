from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2",
)

def generate_answer(question, context_chunks):

    context = "\n".join(context_chunks)

    prompt = f"""
You are a strict document assistant.

RULES:
- Answer ONLY from context
- Do NOT pretend or invent information
- If context is unclear, say "Not found in document"

Context:
{context}

Question:
{question}

Answer in 2-4 simple lines:
"""

    output = generator(
        prompt,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )[0]["generated_text"]

    # clean response (remove prompt repetition)
    answer = output.split("Answer in simple points:")[-1]

    return answer.strip()