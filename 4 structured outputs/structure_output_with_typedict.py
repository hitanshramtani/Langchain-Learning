from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict, Annotated,Optional , Literal
model = ChatOpenAI(model="gpt-4o-mini")

#schema for the response
class review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str,"a brief summary of the review"]
    # action: Annotated[str,"the action to be taken"]
    sentiment: Annotated[Literal["pos","neg"],"the sentiment of the review either postive or negative or neutral"]
    rating: Annotated[int,"the rating of the review out of 10"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    

structured_model = model.with_structured_output(review)


# result  = structured_model.invoke("""The Dell XPS 15 (2023) is a beautiful mix of power and elegance. 
# The 4K OLED display is stunning, making everything from work to movies look incredible. Performance is top-notch with Intel’s latest processors and RTX graphics, handling heavy tasks like a champ. Battery life is decent, though intensive work drains it faster. It’s a bit pricey, but if you want a premium laptop that feels as good as it looks, this one’s worth it.""")

# result  = structured_model.invoke("steps to download the whataspp again")

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Hitansh
""")
print(result)
print(result["key_themes"])
print(result["summary"])
print(result["sentiment"])
print(result["rating"])
