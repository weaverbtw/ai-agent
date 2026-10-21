import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

load_dotenv()

def main():

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("api key does not exist")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key = api_key
    )
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    

    messages = [
            {"role": "user", "content": args.user_prompt},
        ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages, # type: ignore
    )

    if response.usage is None:
        raise RuntimeError("you are out of tokens")
    if args.verbose:
        print(f"User prompt: {messages}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
