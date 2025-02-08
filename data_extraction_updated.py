from langchain.document_loaders import UnstructuredURLLoader

# URL to extract data from
url = "https://brainlox.com/courses/category/technical"

# Load data from the URL
loader = UnstructuredURLLoader(urls=[url])
data = loader.load()

# Save the extracted data to a file
with open('extracted_data.txt', 'w', encoding='utf-8') as f:
    for document in data:
        f.write(document.page_content + "\n")

print("Data extraction complete. Check 'extracted_data.txt' for the output.")
