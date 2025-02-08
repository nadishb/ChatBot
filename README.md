# Brainlox Course Chatbot

A custom chatbot built using Langchain and HuggingFace models that can answer questions about courses from Brainlox's technical courses catalog.

## Features

- Web scraping of course data from Brainlox using BeautifulSoup
- Document embeddings using HuggingFace's sentence-transformers
- Vector storage using Chroma DB
- Text generation using Facebook's BlenderBot model
- RESTful API using Flask

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python main.py
```

2. Load the course data (required before chatting):
```bash
curl -X POST http://localhost:5000/load
```

3. Start chatting with the bot:
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What courses are available in machine learning?"}'
```

## API Endpoints

### POST /load
Loads and processes the course data from Brainlox. Must be called before using the chat endpoint.

**Response:**
```json
{
    "message": "Data loaded successfully"
}
```

### POST /chat
Handles chat interactions with the bot.

**Request Body:**
```json
{
    "query": "Your question here"
}
```

**Response:**
```json
{
    "response": "Bot's response",
    "sources": [
        {
            "content": "Source content",
            "metadata": {
                "source": "URL",
                "title": "Course title"
            }
        }
    ]
}
```

## Project Structure

```
.
├── README.md
├── requirements.txt
├── main.py
└── src/
    ├── api.py          # Flask RESTful API
    ├── scraper.py      # Web scraping module
    ├── embeddings.py   # Vector store and embeddings
    └── chatbot.py      # Chat processing module
```

## Models Used

- Embeddings: sentence-transformers/all-MiniLM-L6-v2
- Text Generation: facebook/blenderbot-400M-distill

## Notes

- The chatbot uses CPU by default for inference. For better performance, you can use GPU if available.
- The vector store is persisted locally in the 'vectorstore' directory.
- Make sure you have a stable internet connection for the initial data loading process.

## Error Handling

The API includes error handling for common scenarios:
- Data not loaded
- Invalid requests
- Processing errors

Each error response includes a meaningful message to help identify the issue.
