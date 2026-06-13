from src.services.gemini_service import get_gemini_client

client = get_gemini_client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Say hello in one sentence."
)

print(response.text)
