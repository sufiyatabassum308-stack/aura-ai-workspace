def split_text_into_chunks(text: str):
    words = text.split()
    chunks = []

    chunk_size = 200

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks