# from langchain.schema.runnable import RunnableLambda
# def word_counter(list):
#     return len(list.split())
# runnanle_word_counter = RunnableLambda(word_counter)
# result = runnanle_word_counter.invoke("hi how are you what is diffrence")
# print(result)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough , RunnableLambda
from langchain_core.output_parsers import StrOutputParser

def word_counter(list):
    return len(list.split())
runnanle_word_counter = RunnableLambda(word_counter)

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate(
    template= "write a Joke about \n {topic}",
    input_variables = ["topic"]
)

parser = StrOutputParser()

chain1 = RunnableSequence(
    prompt, llm , parser
)


parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "Word_count" : runnanle_word_counter
})

final_chain = RunnableSequence(
    chain1, parallel_chain
)
result = final_chain.invoke({"topic":"rcb"})
print(result)