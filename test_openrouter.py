from src.services.openrouter_service import get_openrouter_client

client = get_openrouter_client()

response = client.chat.completions.create(
    model="openrouter/auto",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

print(response.choices[0].message.content)