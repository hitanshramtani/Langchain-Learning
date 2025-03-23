from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="test_generation"
)

model =ChatHuggingFace(llm = llm)
result = model.invoke("who is pm of india")
print(result.content)