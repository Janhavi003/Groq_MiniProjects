import groq
import json
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("API_KEY")

# Ensure the API key is retrieved correctly
if not api_key:
    raise ValueError("API_KEY is missing in environment variables.")

# Initialize the groq client with the API key from the .env file
groq_client = groq.Client(api_key=api_key)

email_body = """
Hi team,

I hope this email finds you well. I wanted to provide you all with an update on our project. We have completed the initial design phase successfully, and we are now moving into the development phase.

During the design phase, our team has put in a lot of effort and creativity to come up with innovative solutions to meet our project goals. I'm truly impressed with the collaboration, dedication, and ideas everyone has contributed.

Moving forward, I would like to request everyone to review the design documents. These documents will help you understand the project requirements, functionality, and the scope of work for the development phase. Please take some time to thoroughly go through them, as it will greatly enhance our collaboration during this phase.

Action Items:

1. Please find attached the design documents. If you have any questions or concerns, feel free to reach out to me or the relevant team members.

2. We need to schedule a kickoff meeting to discuss the development phase and assign responsibilities. I will send out a separate email later today to find a suitable time for the meeting.

Finally, I want to express my appreciation for everyone's hard work so far. I am positive that with our collective efforts, the development phase will be just as successful as the design phase. Let's keep up the good work and continue to fulfill our project objectives.

Thank you all, and have a productive day ahead!

Best regards,

Bill Gates
"""

try:
    # Use the new recommended model for generating completions (example model)
    response = groq_client.chat.completions.create(
        model="mistral-saba-24b",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant which always responds in JSON"},
            {"role": "user", "content": f"Respond in JSON format. Analyze the following email and extract the key action items, a summary of the email, the recipients, and the sender of the email in JSON format. The output format should be: {{\"key_action_items\":[], \"summary\":\"\", \"sender\":\"\", \"receiver\":\"\"}}. Here is the email: {email_body}"},
        ],
    )

    output_json = response.choices[0].message.content

    # Ensure JSON is formatted correctly
    output_json = re.sub(r"\\_", "_", output_json)

    try:
        parsed_json = json.loads(output_json)
        print(json.dumps(parsed_json, indent=4))
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        match = re.search(r'\{.*\}', output_json, re.DOTALL)
        if match:
            try:
                parsed_json = json.loads(match.group())
                print(json.dumps(parsed_json, indent=4))
            except json.JSONDecodeError:
                print("Still unable to parse JSON.")
        else:
            print("No valid JSON found in response.")

except groq.BadRequestError as e:
    print(f"BadRequestError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
