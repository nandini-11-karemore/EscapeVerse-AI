import os
import json

from dotenv import load_dotenv # type: ignore
from google import genai

from ai.prompts import GAME_MASTER_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class AIEngine:

    def process(self, game, action):

        prompt = f"""
{GAME_MASTER_PROMPT}

Current Location:
{game.current_location}

Current Story:
{game.story}

Inventory:
{game.inventory}

Journal:
{game.journal}

Visible Objects:

{", ".join([obj.split(" ",1)[1] if " " in obj else obj for obj in game.visible_objects])}

Previous Events:
{game.history[-10:]} 

Player Action:
{action}
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        # Remove markdown if Gemini returns it
        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        try:
            return json.loads(text)
        except json.JSONDecodeError :
            print("Gemini returned invalid JSON:")
            print(text)

            return {
         "story": "The AI got confused for a moment. Please try that action again.",
        "inventory_add": [],
        "journal_add": [],
        "visible_objects": game.visible_objects,
        "objective_completed": [],
        "location": game.current_location,
        "score": 0
    }
    
def get_hint(self, game):

    prompt = f"""
Give ONE subtle hint.

Current Story:

{game.story}

Inventory:

{game.inventory}

Do NOT reveal the solution.

Keep it under 20 words.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text