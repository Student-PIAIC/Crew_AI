from litellm import completion
import os

os.environ["GEMINI_API_KEY"] = "AIzaSyCrJWUtzJgg3dx1b5qzf-0weXd1Y7aGUBE"

def call_gemini():
    response = completion(
    model="gemini/gemini-1.5-pro",
    messages=[{ "content": "Hello, how are you?","role": "user"}]
    )
    print(response['choices'][0]['message']['content'])

def call_gemini2():
    response = completion(
    model="gemini/gemini-2.0-flash-exp",
    messages=[{ "content": "who is the founder of PIAIC?","role": "user"}]
    )
    print(response['choices'][0]['message']['content'])