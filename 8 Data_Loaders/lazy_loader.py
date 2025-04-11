from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
import time
loader = DirectoryLoader(
    path=r'C:\Users\hitan\Desktop\coding\dl\new_trials\books',
    glob='**/*',
    loader_cls=PyPDFLoader
)
start = time.time()
docs = loader.load()

for document in docs:
    print(document.metadata)
end = time.time()
print(end-start)

time.sleep(1)
#where as lazy loader
start = time.time()
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
end = time.time()
print(end-start)