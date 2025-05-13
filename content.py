import groq
from dotenv import load_dotenv
import os

# Load the API key from .env file
load_dotenv()

def generate_blog_post():
    # Get the API key from environment variables
    api_key = os.getenv("api_key")
    
    # Initialize the Groq client with the API key
    client = groq.Client(api_key=api_key)

    prompt = (
        "Write a blog post titled 'The Art of Relaxation with Blissful Candles'. "
        "Introduce Blissful Candles, describe the variety of scented candles available, "
        "and explain how they help create a relaxing atmosphere. Make the tone warm and inviting."
    )
    
    # Use the new recommended model for generating content
    response = client.chat.completions.create(
        model="mistral-saba-24b",  
        messages=[{"role": "system", "content": "You are a professional blog writer."},
                  {"role": "user", "content": prompt}],
        max_tokens=1000
    )
    
    # Extract the blog content from the response
    blog_post = response.choices[0].message.content
    return blog_post

if __name__ == "__main__":
    blog_content = generate_blog_post()
    print(blog_content)
