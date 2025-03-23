print("langchain chat model")
import getpass
import os

# os.environ["OPENAI_API_KEY"] = "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"

# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="gpt-4o-mini")
# result = llm.invoke("hello")



import ollama

messages = [
    {"role": "user", "content": "Write a Python function to check if a number is prime, dont put commnets to it."}
]

response = ollama.chat(model="deepseek-coder", messages=messages)
print(response["message"])


# from langchain_google_vertexai import ChatVertexAI
# # """
# # C:\Users\hitan\AppData\Roaming\gcloud\application_default_credentials.json
# # """
# API_KEY = "AIzaSyBoqU-AXxC3qeINK7O3kJDCwCpA0mtTIKk"
# PROJECT_ID = "gen-lang-client-0688136157"
# model = ChatVertexAI(
#     model="gemini-2.0-flash-001",
#     project=PROJECT_ID,
#     credentials=API_KEY,  # Using API Key authentication
# )
# # model = ChatVertexAI("gemini-2.0-flash-001", credentials = API_KEY, project="gen-lang-client-0688136157" , model_provider="google_vertexai")
# result = model.invoke("Hello, world!")
# print(result)


# print(result)
print("sucess") 