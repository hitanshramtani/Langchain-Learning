from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini",max_completion_tokens=100)

chat_history = [
    SystemMessage(content="You are a ai chatbot")
]

while(True):
    user_input = input("You: ")
    # instead of making these dictionaries, you can use predefined classes like ChatMessage - SystemMessage, HumanMessage, AiMessage
    # chat_history.append({"role": "human", "content": user_input})
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    # chat_history.append({"role": "ai", "content": result.content})
    chat_history.append(AIMessage(content=result.content)) 
    print("AI: ", result.content)
print("Chat Ended")
print("Chat History: ", chat_history)

