from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini")
prompt1 = PromptTemplate(
    template= "write a Joke about \n {topic}",
    input_variables = ["topic"]
)
prompt2 = PromptTemplate(
    template="explain the joke in detail \n {text}",
    input_variables = ["text"]
)

parser = StrOutputParser()
chain = RunnableSequence(
    prompt1, llm , parser
)

result = chain.invoke({"topic":"csk"})
print(result)

chain2 = RunnableSequence(
    prompt2, llm , parser
)
chain3 = RunnableSequence(
    chain, chain2
)
result2 = chain3.invoke({"topic":"csk"})
print(result2)

# i tried to make it complex but it is not working as expected
# normally result = chain2.invoke({"text": result}) isse bhi kaam chaljata mene ek nayi chain bandi text = result ki jagah nahi chai hehe