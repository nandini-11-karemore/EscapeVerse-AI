class GameEngine:

    def process_action(self, game, action):

        action = action.lower().strip()

        if action == "inspect computer":

            game.story = """
The computer flickers to life.

A hidden drawer opens.

Inside you discover a brass key.
"""

            if "🗝 Brass Key" not in game.inventory:
                game.inventory.append("🗝 Brass Key")

            game.journal.append(
                "Found a hidden brass key inside the computer desk."
            )

        elif action == "inspect bookshelf":

            game.story = """
The bookshelf is covered in dust.

One old astronomy journal catches your attention.
"""

            if "📖 Astronomy Journal" not in game.inventory:
                game.inventory.append("📖 Astronomy Journal")

            game.journal.append(
                "Discovered an old astronomy journal."
            )

        elif action == "look around":

            game.story = """
The room is silent.

You notice:

🖥 Computer

📚 Bookshelf

🌌 Window

🪑 Chair

The rain continues outside.
"""

        else:

            game.story = f"""
You try to '{action}'.

Nothing interesting happens.
"""