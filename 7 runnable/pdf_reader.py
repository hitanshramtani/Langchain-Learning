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
print(f"Total documents in vector store: {len(vectorstore.docstore._dict)}")


retriever = vectorstore.as_retriever(search_kwargs={"k": 5})#search_kwargs={"score_threshold":0.1}


query = input("Ask the query for the document: ")
retrieved_docs = retriever.invoke(query)


retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])


from langchain_openai import ChatOpenAI
llm  = ChatOpenAI(model = "gpt-4o-mini")
from langchain.prompts import PromptTemplate


if not retrieved_text.strip():
    print( "⚠️ No relevant information found in the document.")

else:
    template = PromptTemplate(
        template = "Based on the following text, answer the question: {query} \n\n {retrieved_text}",
        input_variables=["query", "retrieved_text"]
    )
    prompt = template.format(query = query, retrieved_text = retrieved_text)
    result = llm.invoke(prompt)
    print(result.content)
