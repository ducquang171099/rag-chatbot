from langchain.prompts import ChatPromptTemplate
from config import APP_CONFIG

PROMPT_TEMPLATE = """
You are a helpful banking assistant.

Answer the user's question using only the following context.

If the context is not enough, say "I don't know based on the provided information".

Be detailed and clear. Provide explanations if needed.

Context:
{context}

---

Question: {question}
"""

class Chatbot:
    def __init__(self, db, model):
        self.db = db
        self.model = model

    def greet(self):
        return "Hi, I'm Banking Credit Chatbot"

    def ask(self, question):
        # k is the number of results to return
        results = self.db.similarity_search_with_relevance_scores(question, k=4)
        print(results)

        # if the relevance score of the first result is less than PREDICT_RATE, return
        if len(results) == 0 or results[0][1] <= APP_CONFIG["PREDICT_RATE"]:
            print(f"Unable to find matching results for {question}")
            return ''

        # create the prompt for the chatbot
        context = "\n\n---\n\n".join([doc.page_content for doc, score in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context, question=question)
        print(prompt)

        # the LLM uses the prompt to answer the question
        invoke_response = self.model.invoke(prompt)

        return invoke_response["response"]
