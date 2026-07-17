from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
# print(os.getenv("GEMINI_API_KEY"))

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.0-flash-lite-001",
    contents = "Explain FastAPI in simple words"
)

end = time.time()

print(response.text)
print(f"\nResponse Time: {end - start:.2f} seconds")