from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
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

joke_chain = RunnableSequence(prompt1 | llm | parser)

parralel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explain": RunnableSequence(prompt2 | llm | parser)
})

final_chain = RunnableSequence(
    joke_chain,
    parralel_chain
)
print(final_chain.invoke({"topic":"csk and rcb"}))