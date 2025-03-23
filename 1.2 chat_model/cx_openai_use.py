from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini",max_completion_tokens=100) # temprature , max_completion_token
result = llm.invoke("what is ai")
print(result.content)