import openai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(input_text):
    try:
        print(openai.api_key)
        # Call the OpenAI Chat API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content":input_text}
            ]
        )
        # Extract the summary from the response
        summary = response["choices"][0]["message"]["content"].strip()
        print("Summary:", summary)
        return summary
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    input_text = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."
    summarize_text(input_text)



