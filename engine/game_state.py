class GameState:

    def __init__(self):

        self.location = "Observatory"

        self.health = 100

        self.score = 0

        self.inventory = []

        self.journal = [
            "You wake up inside an abandoned observatory."
        ]

        self.objectives = [
            "Explore the Observatory",
            "Inspect the Computer",
            "Escape"
        ]

        self.story = """
You slowly wake up inside an abandoned observatory.

Rain taps gently against the large window.

A computer screen flickers in the darkness.

Something feels unfinished.
"""

        self.visible_objects = [
            "🖥 Computer",
            "📚 Bookshelf",
            "🪑 Chair",
            "🌌 Window",
            "📅 Calendar"
        ]