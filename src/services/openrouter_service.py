import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_openrouter_client():

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    return client