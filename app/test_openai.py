import openai

# Replace this with your OpenAI API Key
#openai.api_key = ""

# Test request
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize this: Python is a programming language..."}
    ]
)

print(response.choices[0].message.content)