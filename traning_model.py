import os
import shutil
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import APP_CONFIG

def traning_model():
    documents = load_documents()
    chunks = split_text(documents)

    save_to_chroma(chunks)

def load_documents():
    loader = DirectoryLoader(APP_CONFIG["TRAINING_FOLDER_PATH"], glob="*")
    documents = loader.load()

    return documents

def split_text(documents):
    """This function will split the documents into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    if len(chunks) > 20:
        document = chunks[20]
        print(document.page_content)
        print(document.metadata)
    else:
        document = chunks[0]
        print(document.page_content)
        print(document.metadata)

    return chunks

def save_to_chroma(chunks: list[Document]):
    # Clear out the database directory first
    if os.path.exists(APP_CONFIG["CHROMA_PATH"]):
        shutil.rmtree(APP_CONFIG["CHROMA_PATH"]) # Deletes all files and subdirectories within the specified path.
 
    # Create a vector database from the documents
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(openai_api_key=APP_CONFIG["OPENAI_API_KEY"]), persist_directory=APP_CONFIG["CHROMA_PATH"])
    db.persist() # Saves the database to disk as a SQLite3 file

    print(f"Saved {len(chunks)} chunks to database in {APP_CONFIG["CHROMA_PATH"]}.")

if __name__ == "__main__":
    traning_model()
