from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embedding = OpenAIEmbeddings(model = "text-embedding-3-small", dimensions= 300)
doc = [
    "Virat Kohli is one of the greatest batsmen in Indian cricket history", 
    "MS Dhoni led India to victory in the 2007 T20 World Cup and 2011 ODI World Cup", 
    "Sachin Tendulkar is known as the 'God of Cricket' for his remarkable records", "Rohit Sharma holds the record for the highest individual score in ODI cricket", "Jasprit Bumrah is famous for his deadly yorkers and pace bowling", "Rahul Dravid is called 'The Wall' for his solid batting technique", "Kapil Dev led India to its first World Cup win in 1983", "Yuvraj Singh played a crucial role in India's 2011 World Cup triumph with his all-round performance",
    "Shubman Gill, known for his elegant stroke play and composure at a young age, has emerged as a future leader in Indian cricket", "Yashasvi Jaiswal has captured attention with his aggressive batting and record-breaking domestic performances, symbolizing the rise of a new generation", "KL Rahul’s versatility as a top-order batsman and wicketkeeper has earned him respect for his consistency across formats", "Ravindra Jadeja's exceptional all-round abilities—from sharp fielding to effective spin bowling—make him an indispensable asset for Team India", "Hardik Pandya brings dynamism and balance to the side with his explosive batting and medium-fast bowling skills", "Sourav Ganguly revolutionized Indian cricket with his fearless captaincy and innovative leadership, inspiring a generation of cricketers", "Anil Kumble’s masterful leg-spin and tactical acumen set enduring benchmarks in the history of Indian cricket",
    "Emerging Talent on the Rise – India: Young stars like Yashasvi Jaiswal and Shubman Gill are breaking records in domestic cricket and the IPL, promising to lead the next generation of Indian cricketers", "Veteran Milestones – India: Established icons such as Virat Kohli, Rohit Sharma, and Jasprit Bumrah continue to anchor the team with their consistent performances and leadership, inspiring budding talents across the country", "Contract and Squad Updates – India: The BCCI’s recent central contract announcements highlight rising market values, with emerging players now securing lucrative deals alongside seasoned stars", "Domestic Leagues Impact – India: The IPL remains a pivotal platform where exceptional performances propel players into the international spotlight and accelerate their career trajectories", "Technological Advancements – India: Indian cricket is embracing modern analytics and video technology to refine player techniques and strategize better on the international stage"
]
query = "who is yashasvi jeswal"
doc_embedding = embedding.embed_documents(doc)
query_embedding = embedding.embed_query(query)
scores = cosine_similarity([query_embedding],doc_embedding)[0]
index, score = sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]
print(query)
print(doc[index])