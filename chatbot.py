import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def chatbot():
    chat = ChatGroq(api_key=os.getenv("API_KEY"), model="llama3-8b-8192", temperature=0)

    promp = ChatPromptTemplate.from_messages([
        ("system", "Voçê é um Assistente amigável"),
        ("human", "{input}")    
    ])

    chain = promp | chat

    user = input("Você: ")

    while user != "sair":
        reponse = chain.invoke({"input": user})
        print(f"IA: {reponse.content}")
        print("Se deseja sair digite 'sair' ")
        user = input("Voçê: ").lower()

if __name__ == "__main__":
    chatbot()