from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import APP_CONFIG
from chatbot import Chatbot
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def chatbot_response(query_text):
    # Register DB
    db = Chroma(persist_directory=APP_CONFIG["CHROMA_PATH"], embedding_function=OpenAIEmbeddings())
    # Register AI LLM
    llm = ChatOpenAI(
        openai_api_key=APP_CONFIG["OPENAI_API_KEY"],
        model_name="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens=1024,
    )

    # Memory setup
    memory = ConversationBufferMemory()

    # Conversation chain
    chain = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    # Create Chatbot instance
    chatbot = Chatbot(db, chain)

    return chatbot.ask(query_text)
