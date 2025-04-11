from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import APP_CONFIG
from chatbot import Chatbot
from langchain_openai import ChatOpenAI

def chatbot_response(query_text):
    # Register DB
    db = Chroma(persist_directory=APP_CONFIG["CHROMA_PATH"], embedding_function=OpenAIEmbeddings())
    # Register AI LLM
    model = ChatOpenAI()
    # Create Chatbot instance
    chatbot = Chatbot(db, model)

    return chatbot.ask(query_text)
