from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path=r'C:\Users\hitan\Desktop\coding\dl\new_trials\books',
    glob='**/*',
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(len(docs))
print(docs[0].page_content[:10])
print(docs[0].metadata)
# for document in docs:
#     print(document.metadata[''])