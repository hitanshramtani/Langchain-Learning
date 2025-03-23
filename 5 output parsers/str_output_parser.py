from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


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

parser = StrOutputParser()
chain = template1 | llm | parser |template2|llm|parser
result = chain.invoke({"topic" : "Black Hole"})
print(result)