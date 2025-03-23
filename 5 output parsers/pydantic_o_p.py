from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
class person(BaseModel):
    name: str = Field(discription="Name of the person")
    age: int = Field(discription="Age of the person and it should be greater than 18")
    city: str = Field(discription="City of the person and it should be north indian ")
    description: str
parser = PydanticOutputParser(pydantic_object=person)
template = PromptTemplate(
    template='Genrate me a name age and city of random north indian person and describe him \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# using chain
# chain = template | llm | parser
# result = chain.invoke({}) 
# print(result)

# without chain 
prompt = template.format()
# print(prompt)
result = llm.invoke(prompt)
print(result.content)
print(parser.parse(result.content))