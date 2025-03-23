from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser , ResponseSchema

load_dotenv()
parser = JsonOutputParser()
llm  = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
Schema = [
    ResponseSchema(name = "fact1", description= " fact 1 about the topic"),
    ResponseSchema(name = "fact2", description= " fact 2 about the topic"),
    ResponseSchema(name = "fact3", description= " fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(Schema)
template = PromptTemplate(
    template='Give me 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
prompt = template.format(topic = "blackhole")
print(prompt)
result = llm.invoke(prompt) 
print(result.content)
print(parser.parse(result.content))