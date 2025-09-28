import os, sys
from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    user_prompt = ""
    verbose = False
    if len(sys.argv) < 2 :
        print("Error, prompt required")
        sys.exit(1)
    else :
        user_prompt = sys.argv[1]
    if "--verbose" in sys.argv:
        verbose = True
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    if verbose :
        print("User prompt:", user_prompt)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )
    if verbose :
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
