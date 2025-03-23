from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
llm  = ChatOpenAI(model="gpt-4o-mini")


# 1st prompt -> Detailed Report 
template1 = PromptTemplate(
    template="write a detailed rreport on {topic}",
    input_variables=['topic']
)

# 2nd prompt -> Summary
template2 = PromptTemplate(
    template="write a 5 line summory on the following text. /n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({"topic" : "Black Hole"})
result = llm.invoke(prompt1)
prompt2 = template2.invoke({'text':result.content})
result1 = llm.invoke(prompt2)
print(result1.content)
