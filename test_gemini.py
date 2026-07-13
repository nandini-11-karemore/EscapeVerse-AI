import os
import json
from dotenv import load_dotenv # type: ignore
from google import genai

from ai.prompts import GAME_MASTER_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

prompt = f"""
{GAME_MASTER_PROMPT}

Current Location:
Observatory

Inventory:
[]

Journal:
[]

Visible Objects:
Computer, Bookshelf, Window

Player Action:
inspect computer
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)

try:
    data = json.loads(response.text)
    print("\n✅ JSON parsed successfully!")
    print(data)
except Exception as e:
    print("\n❌ JSON parsing failed")
    print(e)