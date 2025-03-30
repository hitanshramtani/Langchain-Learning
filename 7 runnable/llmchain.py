from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = PromptTemplate(
    template = "Genrate 5 intresting facts about {name}",
    input_variables = ["name"]
)
from langchain.chains import LLMChain
chain  = LLMChain(
    llm = llm,
    prompt = prompt
)
result = chain.run({"name":"cricket"})
print(result)