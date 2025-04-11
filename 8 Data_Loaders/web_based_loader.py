from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
url = "https://www.amazon.in/s?k=shoes+for+men&ref=nb_sb_noss"
# url2 = "https://dizy.in/team"
loader = WebBaseLoader(url)

docs = loader.load()
# print(len(docs))
# print(docs[1].page_content)
load_dotenv()

model = ChatOpenAI(model  = "gpt-4o-mini")

prompt = PromptTemplate(
    template='Answer the following question - \n {question} \n from the text \n{text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

chain = prompt | model | parser
question = input("Enter your question regarding the shoes for men at amazon: ")
result = chain.invoke({'question': question,'text': docs[0].page_content})
print(result)