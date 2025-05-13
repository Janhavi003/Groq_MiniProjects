import groq
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.getenv("API_KEY") 

# Ensure the API key is loaded correctly
if API_KEY is None:
    raise ValueError("API key not found. Please make sure your .env file is set up correctly.")

# Initialize the Groq client with the API key
client = groq.Client(api_key=API_KEY)

# Let's assume that 'long_article' contains the text of the article that you want to summarize.
long_article = """
The Beauty of Imperfection: Finding Art in the Flaws
Perfection is often seen as the ultimate goal. We strive for flawless performances, ideal appearances, and impeccable execution. Yet, true beauty often lies in imperfection. The Japanese philosophy of wabi-sabi celebrates the transient, the incomplete, and the imperfect—finding grace in the cracks of existence.

From the jagged edges of a broken vase repaired with gold in kintsugi to the asymmetry of a handcrafted sculpture, imperfection tells a story. It is in the flaws that we find authenticity, depth, and meaning. A perfectly symmetrical face may be pleasing, but it is the slight irregularities that make a person unique.

In poetry, imperfection breathes life into words. A poem with uneven rhythm can still evoke powerful emotions. A verse that breaks conventional structure can resonate deeply, simply because it is raw and real. Art is not about perfection; it is about expression.

So why do we fear imperfection? Society conditions us to seek polished results, but some of the greatest discoveries—penicillin, microwave ovens, even Post-it notes—were born from mistakes. Flaws are not failures; they are opportunities.

Embracing imperfection allows us to see the world differently. Instead of hiding mistakes, we can highlight them. Instead of discarding the broken, we can mend it beautifully. Life is not a perfect script, and that is precisely what makes it worth experiencing.

Imperfection is not a flaw; it is a feature.
"""

# Make the API request to summarize the article
response = client.chat.completions.create(
    model="mistral-saba-24b", 
    messages=[{"role": "user", "content": f"Summarize this article in less than 200 words:\n\n{long_article}"}],
    max_tokens=200,  
    temperature=0,  
)

# Correctly access the generated summary from the response
summary = response.choices[0].message.content.strip()  

# Output the summary and word count
print(f"Summary:\n{summary}")
print(f"\nSummary word count: {len(summary.split())}")
