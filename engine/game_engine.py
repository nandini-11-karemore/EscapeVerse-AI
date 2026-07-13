from ai.ai_engine import AIEngine


class GameEngine:

    def __init__(self):
        self.ai = AIEngine()

    def process_action(self, game, action):

        response = self.ai.process(game, action)
        game.history.append({
        "player": action,
        "story": response["story"]
        })
        if response["location"]:
         game.current_location = response["location"]

        game.score += response.get("score", 0)
        # Update Story
        game.story = response["story"]

        # Update Inventory
        for item in response["inventory_add"]:
            if item not in game.inventory:
                game.inventory.append(item)

        # Update Journal
        for note in response["journal_add"]:
            if note not in game.journal:
                game.journal.append(note)

        # Update Visible Objects
        if response["visible_objects"]:
            game.visible_objects = response["visible_objects"] 
def get_hint(self, game):

    response = self.ai.get_hint(game)

    return response