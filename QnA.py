import os
from dotenv import load_dotenv
import groq

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variable (for security reasons)
API_KEY = os.getenv("API_KEY")

# Ensure the API key is loaded correctly
if not API_KEY:
    raise ValueError("API_KEY is missing in the environment variables.")

# Initialize the Groq client with the API key
client = groq.Client(api_key=API_KEY)

# Define the news article summary
article_summary = """
Apple is expanding its manufacturing operations in India, with exports increasing significantly.
Smartphone exports in India surged by nearly 50% in the first 10 months of the fiscal year, with Apple playing a crucial role.
Foxconn and Tata Electronics produce various Apple products in India, including the high-end iPhone 16 Pro.
This growth aligns with India's "Make in India" subsidy scheme, resulting in mobile phones becoming India's biggest export, surpassing diamonds.
Apple's strategic shift to Indian manufacturing is partly due to challenges arising from its dependence on China amidst rising US-China tensions.
Expanding production in India allows Apple to offer competitive prices by avoiding customs duties.
Additionally, India's high-income earners are allocating a larger portion of their income to loan repayments, unlike lower-income groups who save more.
This trend reflects changing spending attitudes in India.
The Reserve Bank of India has reported a decline in foreign direct investment for the first nine months of the fiscal year.
"""

# Define the questions for the Q&A session
questions = [
    "What are the main reasons behind Apple's expansion of manufacturing in India?",
    "How has India's 'Make in India' initiative influenced Apple's manufacturing decisions?",
    "What impact has Apple's manufacturing shift had on India's export economy?",
    "How are spending habits changing among India's high-income earners?",
    "What recent trends have been observed in foreign direct investment in India?"
]

# Function to generate answers using Groq API
def generate_answer(question, context):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
            ],
            model="mistral-saba-24b",  
            max_tokens=500,  
            temperature=0.7  
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Conduct the Q&A session
for idx, question in enumerate(questions, 1):
    answer = generate_answer(question, article_summary)
    print(f"Q{idx}: {question}")
    print(f"A{idx}: {answer}\n")
