import faiss
import numpy as np

# FAISS dimension for all-MiniLM-L6-v2 embeddings
dimension = 384

# FAISS index (L2 distance)
index = faiss.IndexFlatL2(dimension)

# Stores actual text chunks
stored_chunks = []


def add_to_vector_store(chunks, embeddings):
    """
    Store embeddings in FAISS + keep chunk mapping
    """

    global stored_chunks, index

    if chunks is None or embeddings is None:
        return 0

    if len(chunks) == 0 or len(embeddings) == 0:
        return 0

    embeddings = np.array(embeddings).astype("float32")

    # Safety check: embeddings must match chunks
    if len(embeddings) != len(chunks):
        min_len = min(len(embeddings), len(chunks))
        embeddings = embeddings[:min_len]
        chunks = chunks[:min_len]

    index.add(embeddings)
    stored_chunks.extend(chunks)

    return len(stored_chunks)


def search(query_embedding, top_k=3):
    """
    Search similar chunks from FAISS index
    """

    global stored_chunks, index

    # If no data uploaded yet
    if len(stored_chunks) == 0:
        return ["No document uploaded yet"]

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in indices[0]:
        if 0 <= i < len(stored_chunks):
            chunk_text = stored_chunks[i]

            results.append({
    "text": chunk_text,
    "source": f"Chunk {i+1}",
    "preview": chunk_text[:120] + "..."
})

    return results