from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions=32)
result =embedding.embed_query("delhi is the capital of india")
print(str(result))

# if iwant to create embedding of multiple files
# just in result = embedding.embed_documents(doc)