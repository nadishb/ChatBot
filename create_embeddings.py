import faiss
import numpy as np
from langchain.embeddings import SentenceTransformerEmbeddings

# Load extracted data
with open('extracted_data.txt', 'r', encoding='utf-8') as f:
    documents = f.readlines()

# Create embeddings
embeddings = SentenceTransformerEmbeddings()
document_embeddings = embeddings.embed_documents(documents)

# Convert to numpy array
document_embeddings_np = np.array(document_embeddings).astype('float32')

# Create a FAISS index
index = faiss.IndexFlatL2(document_embeddings_np.shape[1])
index.add(document_embeddings_np)

# Save the index to a file
faiss.write_index(index, 'faiss_index.index')

print("Embeddings created and stored in 'faiss_index.index'.")
