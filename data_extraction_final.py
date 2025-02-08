from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load the webpage content
loader = WebBaseLoader("https://brainlox.com/courses/category/technical")
docs = loader.load()

# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_documents(docs)

print(f"Extracted {len(documents)} chunks from the website.")

