from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

# from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
# loader = TextLoader("doc.txt")
doc_address = r"C:\Users\hitan\Desktop\coding\dl\new_trials\ai-04-00053.pdf"
loader = PyMuPDFLoader(doc_address)
documents = loader.load()


from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
docs = text_splitter.split_documents(documents)


from langchain_community.vectorstores import FAISS
embedding = OpenAIEmbeddings(model = "text-embedding-3-large")
vectorstore = FAISS.from_documents(docs,embedding)

retriever = vectorstore.as_retriever(search_kwargs={"k": 5})


from langchain_openai import ChatOpenAI
llm  = ChatOpenAI(model = "gpt-4o-mini")


from langchain.chains import RetrievalQA
qa_chain = RetrievalQA.from_chain_type(llm = llm, retriever = retriever)

query = input("Ask the query for the document: ")
ans = qa_chain.run(query)
print(ans)