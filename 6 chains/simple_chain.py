from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = PromptTemplate(
    template = "Genrate 5 intresting facts about {name}",
    input_variables = ["name"]
)

from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

chain = prompt | llm | parser #  | pipe operator ( LCEL)

result = chain.invoke({"name":"cricket"})
print(result)

chain.get_graph().print_ascii()
