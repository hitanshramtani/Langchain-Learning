from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model  = ChatOpenAI(model="gpt-4o-mini",max_completion_tokens=100)
messages = [
    SystemMessage(content="You are a ai chatbot"),
    HumanMessage(content="What is langchain in two lines")
]
result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)