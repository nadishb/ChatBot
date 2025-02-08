from flask import Flask, request, jsonify
import faiss
import numpy as np
from langchain.embeddings import SentenceTransformerEmbeddings

app = Flask(__name__)

# Load the FAISS index
index = faiss.read_index('faiss_index.index')
embeddings = SentenceTransformerEmbeddings()

@app.route('/query', methods=['POST'])
def query():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    # Create embedding for the user input
    input_embedding = embeddings.embed_query(user_input)

    # Search the index
    input_embedding_np = np.array(input_embedding).astype('float32').reshape(1, -1)
    distances, indices = index.search(input_embedding_np, k=5)  # Get top 5 results

    # Prepare response
    results = []
    for i in range(len(indices[0])):
        results.append({
            'index': indices[0][i],
            'distance': distances[0][i]
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
