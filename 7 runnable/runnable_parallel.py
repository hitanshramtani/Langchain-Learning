from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini")
prompt1 = PromptTemplate(
    template= "Genrate a Linkdin Posit about \n {topic}",
    input_variables = ["topic"]
)
prompt2 = PromptTemplate(
    template="genrate a X post about  \n {topic}",
    input_variables = ["topic"]
)
parser = StrOutputParser()
parrallel_chain = RunnableParallel({
    "linkedin": prompt1 | llm | parser,
    "x": prompt2 | llm | parser
})
# parrallel_chain = RunnableParallel({
#     "linkedin": RunnableSequence(prompt1 | llm | parser),
#     "x": RunnableSequence(prompt2 | llm | parser)
# })

result = parrallel_chain.invoke({"topic": "ai"})
print(result)