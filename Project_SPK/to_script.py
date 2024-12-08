import os
from dotenv import load_dotenv
from together import Together


load_dotenv()


api_key = os.getenv("T_API_KEY")



def translate(str):
    if str is None:
        print("No topic")
        return None
    #print(f"this is the topic {str}")
    client = Together(api_key=api_key)
    response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": f"Create a tweet that is relevant, engaging, and trending,based on the following topic: {str}.The tweet should be 270 characters or less, include trending hashtags (if possible),and be suitable for a wide audience. It should sound casual, clear, and attention-grabbing. Don't add anything else except the tweet"}
    ]
)
    x = response.choices[0].message.content
    #print(x)
    return x

