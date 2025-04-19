import json
import os

def load_json_config(filename):
    path = os.path.join("config", filename)
    with open(path, "r") as f:
        return json.load(f)

UI_CONFIG = load_json_config("ui_config.json")
