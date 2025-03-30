from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model = "gpt-4o-mini")
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate(
    template = "Give a brief(around 5 line) on a topic {topic}",
    input_variables=["topic"]
)
topic = input("Enter the topic name to get a brief about it ")
promptt = prompt.invoke(topic)

result =  llm.invoke(promptt)
print(result.content)