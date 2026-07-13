import os
import json

import google.generativeai as genai # type: ignore
from dotenv import load_dotenv # type: ignore

from ai.prompts import GAME_MASTER_PROMPT

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


class AIEngine:

    def process(self, game, action):

        prompt = f"""
{GAME_MASTER_PROMPT}

Current Location:
{game.location}

Current Story:
{game.story}

Inventory:
{game.inventory}

Journal:
{game.journal}

Visible Objects:
{game.visible_objects}

Player Action:
{action}
"""

        response = model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)
    