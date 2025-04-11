from langchain_community.document_loaders import PyPDFLoader
# from langchain_openai import ChatOpenAI

# from dotenv import load_dotenv
# load_dotenv()

doc_address = r"C:\Users\hitan\Desktop\coding\dl\new_trials\ai-04-00053.pdf"
loader = PyPDFLoader(doc_address)
documents = loader.load()
print(len(documents))
print(documents)
print(documents[0].page_content)
print(documents[0].metadata)