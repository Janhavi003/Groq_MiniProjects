import os
from dotenv import load_dotenv
import groq

# Load the environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
API_KEY = os.getenv("API_KEY")

# Debugging: Ensure the API key is loaded
if not API_KEY:
    raise ValueError("API_KEY is missing or invalid.")

print(f"Loaded API_KEY: {API_KEY}")  

# Initialize the Groq client with the API key
client = groq.Client(api_key=API_KEY)

# Define the received email content
received_email = """
Dear [Your Name],

I recently came across your product, and I'm interested in learning more about it. Could you please provide more details about its features and pricing?

Looking forward to hearing from you soon.

Best regards,  
[Customer's Name]
"""

# Make sure to update the model to a supported one
response = client.chat.completions.create(
    model="mistral-saba-24b", 
    messages=[
        {"role": "system", "content": "You are a professional sales representative for Blissful Candles, a candle manufacturing company."},
        {"role": "user", "content": f"{received_email}\nIn response to the above email, write a professional email explaining our product, Blissful Candles, in a pleasant way and ask the customer for a suitable time to set up a meeting."}
    ],
    max_tokens=500,  
    temperature=0.7,  
)

# Extract and print the email response
email_response = response.choices[0].message.content

print(email_response)
