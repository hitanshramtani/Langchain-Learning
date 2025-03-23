from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template= "genrate a detailed report of the following text \n {topic}",
    input_variables = ["topic"]
)
prompt2 = PromptTemplate(
    template= "genrate the key points from the text \n {text}",
    input_variables = ["text"]
)
llm = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()
chain = prompt1 | llm | parser |  prompt2 | llm | parser

print(chain.invoke({"topic":"make an ai agent which can automaticly upload post on linkdin daily( no code) just methods"}))