from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

loader = TextLoader(r"C:\Users\hitan\Desktop\coding\dl\new_trials\poem.txt",encoding="utf-8")

docs = loader.load()
print(type(docs))
print(len(docs))
# print(docs[0])
print(type(docs[0]))
print(docs[0].metadata)




load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

chain = prompt | model | parser
print(chain.invoke({"poem":docs[0].page_content}))