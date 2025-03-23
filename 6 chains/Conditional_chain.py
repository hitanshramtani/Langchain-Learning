from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive","negative"] =  Field(disciption="Give the sentiment of the feedback")
parser2 = PydanticOutputParser(pydantic_object=Feedback)


llm = ChatOpenAI(model="gpt-4o-mini")
prompt1 = PromptTemplate(
    template= "classify the following text into one of the following categories[positive, Negative] \n {text}\n {format_instruction}",
    input_variables = ["text"],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)

classifier_chain = prompt1 | llm | parser2
# print(classifier_chain.invoke({"text":"I am happy today"}))
prompt2 = PromptTemplate(
    template= "write a appropiate response to this positive feedback \n {feedback}",
    input_variables = ["feedback"]
)
prompt3 = PromptTemplate(
    template= "write a appropiate response to this Negative feedback \n {feedback}",
    input_variables = ["feedback"]
)



branch_chain = RunnableBranch(
    (lambda x:x.sentiment== "positive",prompt2 | llm | parser),
    (lambda x:x.sentiment == "negative",prompt3 | llm | parser),
    RunnableLambda(lambda x: "could not classify the feedback")
)

chain = classifier_chain | branch_chain
print(chain.invoke({"text":"this is a wonderfull phone"}))

