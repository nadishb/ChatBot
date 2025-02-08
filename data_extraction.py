from langchain.document_loaders import UnstructuredURLLoader

# URL to extract data from
url = "https://brainlox.com/courses/category/technical"

# Load data from the URL
loader = UnstructuredURLLoader(urls=[url])
data = loader.load()

# Print the extracted data
for document in data:
    print(document.page_content)
