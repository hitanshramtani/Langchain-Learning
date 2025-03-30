
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough , RunnableLambda , RunnableBranch
from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template = "write a detailed report of {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="write a summary on report {text}",
    input_variables="text"
)
parser = StrOutputParser()

llm = ChatOpenAI(model="gpt-4o-mini")

report_genration_chain = RunnableSequence(prompt1, llm, parser)
branch_chain = RunnableBranch(
    (lambda x : len(x.split())>300,RunnableSequence(prompt2,llm,parser)),#if condition
    RunnablePassthrough()#deafault/ else
)
final_chain = report_genration_chain|branch_chain
result = final_chain.invoke({"topic":"ai"})
print(result)
