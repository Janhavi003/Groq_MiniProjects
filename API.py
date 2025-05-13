from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("API_KEY")

# Check if API key is loaded correctly
if not api_key:
    raise ValueError("API_KEY is missing in environment variables.")

# Optionally, print the API key for debugging (ensure it's correct)
print(f"Using API key: {api_key[:4]}...")  
# Initialize the Groq client with the API key from the .env file
client = Groq(api_key=api_key)

# Prepare the prompt for the Bubble Sort algorithm pseudo-code request
prompt = "Please provide pseudo-code for the Bubble Sort algorithm."

# Create a request to the Groq API
try:
    completion = client.chat.completions.create(
        model="mistral-saba-24b",  
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False, 
        stop=None,
    )

    # Print the result
    print(completion.choices[0].message.content)

except groq.AuthenticationError as e:
    print(f"AuthenticationError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
