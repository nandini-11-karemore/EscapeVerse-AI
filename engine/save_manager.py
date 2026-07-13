import json

SAVE_FILE = "savegame.json"

def save_game(game):

    data = {
        "story": game.story,
        "inventory": game.inventory,
        "journal": game.journal,
        "objectives": game.objectives,
        "visible_objects": game.visible_objects,
        "location": game.current_location,
        "score": game.score,
        "history": game.history
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_game(game):

    try:
        with open(SAVE_FILE) as f:
            data = json.load(f)

        game.story = data["story"]
        game.inventory = data["inventory"]
        game.journal = data["journal"]
        game.objectives = data["objectives"]
        game.visible_objects = data["visible_objects"]
        game.current_location = data["location"]
        game.score = data["score"]
        game.history = data["history"]

        return True

    except:
        return False