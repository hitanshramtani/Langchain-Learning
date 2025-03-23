from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

parser = JsonOutputParser()
llm  = ChatOpenAI(model="gpt-4o-mini")
template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
# topic = "human"
# prompt = template.format(topic = topic)
# print(prompt)
# result = llm.invoke(prompt)
# print(result)
# print("\n\n")
# print(parser.parse(result.content))

chain = template | llm | parser

result = chain.invoke({'topic':'blackhole'})
print(result)