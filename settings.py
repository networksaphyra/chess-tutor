from pathlib import Path
import json

DEFAULT_SETTINGS_FILE = ".settings.json"
DEFAULT_ASSETS_PATH = "assets/classic/"

DEFAULT_SETTINGS = {
    "premove": "off",
    "theme": {
        "board": "classic",
        "pieces": "classic"
    },
    "coordinates": "off",
    "move_method": "click, drag",
    "board": {
        "squares": 8
    },
    "w_pawn": f"{DEFAULT_ASSETS_PATH}w_pawn.png",
    "w_knight": f"{DEFAULT_ASSETS_PATH}w_knight.png",
    "w_bishop": f"{DEFAULT_ASSETS_PATH}w_bishop.png",
    "w_rook": f"{DEFAULT_ASSETS_PATH}w_rook.png",
    "w_queen": f"{DEFAULT_ASSETS_PATH}w_queen.png",
    "w_king": f"{DEFAULT_ASSETS_PATH}w_king.png",
    "b_pawn": f"{DEFAULT_ASSETS_PATH}b_pawn.png",
    "b_knight": f"{DEFAULT_ASSETS_PATH}b_knight.png",
    "b_bishop": f"{DEFAULT_ASSETS_PATH}b_bishop.png",
    "b_rook": f"{DEFAULT_ASSETS_PATH}b_rook.png",
    "b_queen": f"{DEFAULT_ASSETS_PATH}b_queen.png",
    "b_king": f"{DEFAULT_ASSETS_PATH}b_king.png",
}

def update_settings_file(new_data):
    with open(DEFAULT_SETTINGS_FILE, "w") as settings:
        json.dump(new_data, settings, indent=2)
    
def get_settings():
    if not Path(DEFAULT_SETTINGS_FILE).exists():
        update_settings_file(DEFAULT_SETTINGS)

    with open(DEFAULT_SETTINGS_FILE, "r") as file:
        return json.load(file)


# Tests purposes
if __name__ == "__main__":
  current_settings = get_settings()
  print(current_settings)
