import groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variable
api_key = os.getenv("API_KEY")

# Ensure the API key is loaded correctly
if not api_key:
    raise ValueError("API_KEY is missing in the environment variables.")

# Initialize the Groq client with the API key
client = groq.Client(api_key=api_key)

# Your transcript or any content that you want to process
transcript = """CEO: We had a strong quarter with a 20% increase in revenue. 
We launched new products and expanded to new markets. 
Customer satisfaction improved, and we are optimistic about the next quarter."""

# Define chunk size for transcript splitting (if needed)
chunk_size = 2048
chunks = [transcript[i:i + chunk_size] for i in range(0, len(transcript), chunk_size)]

summarization_prompt = "The following is a section of an earnings call report. Help me summarize it. Content:\n\n"

summaries = []

# Process the chunks in case transcript is large
for chunk in chunks:
    response = client.chat.completions.create(
        model="mistral-saba-24b", 
        messages=[{"role": "user", "content": summarization_prompt + chunk}],
        max_tokens=1000,
        temperature=0.5
    )
    
    summary = response.choices[0].message.content
    summaries.append(summary)

# Create a unification prompt to combine all summarized parts
unification_prompt = "Summarize the key points from the earnings call:\n\n" + "\n".join(summaries)

# Final response with the combined summary
final_response = client.chat.completions.create(
    model="mistral-saba-24b",  
    messages=[{"role": "user", "content": unification_prompt}],
    max_tokens=1000,
    temperature=0.5
)

# Final summary output
final_summary = final_response.choices[0].message.content

print(final_summary)
