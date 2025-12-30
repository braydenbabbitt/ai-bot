import os
import argparse
from dotenv import load_dotenv
from google.genai import types

_ = load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if (api_key == None):
    raise RuntimeError("No API key found")

from google import genai


def main():
    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="AI Bot")
    _ = parser.add_argument("user_prompt", type=str, help="User Prompt")
    _ = parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    user_prompt = str(args.user_prompt)  # pyright: ignore[reportAny]
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    res = client.models.generate_content(model="gemini-2.5-flash", contents=messages)
    if (res.usage_metadata == None):
        raise RuntimeError("No metadata")
    if (args.verbose):
        print("User prompt: " + str(user_prompt))
        print("Prompt tokens: " + str(res.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(res.usage_metadata.candidates_token_count))
        print("Response: " + str(res.text))
    else:
        print(str(res.text))


if __name__ == "__main__":
    main()
