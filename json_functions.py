import json
import os

def save_settings_last_applied(ui_element, settings):
    if os.path.exists("last_applied.json"):
        last_applied = json.load(open("last_applied.json"))
        last_applied[ui_element] = settings
        json.dump(last_applied, open("last_applied.json", "w"))
        print("saved last_applied.json")
    else:
        file_name = "last_applied.json"
        settings_dict = {ui_element: settings}
        print(settings_dict)
        # The below to create my json file when it does not exist
        with open(file_name, "w") as f:
            json.dump(settings_dict, f)
        print("saved last_applied.json")

def load_settings_last_applied(ui_element):
    if os.path.exists("last_applied.json"):
        last_applied = json.load(open("last_applied.json"))
        print("loaded last_applied.json")
        return last_applied[ui_element]

def save_settings(ui_element, settings, save_slot):
    file_name = f"saved_settings{save_slot}.json"
    if os.path.exists(f"saved_settings{save_slot}.json"):
        print(settings)
        saved_settings = json.load(open(f"saved_settings{save_slot}.json"))
        saved_settings[ui_element] = settings
        print(saved_settings)
        with open(file_name, "w") as f:
            json.dump(saved_settings, f)
        print(f"saved saved_settings{save_slot}.json")
    else:
        print(settings)
        settings_dict = {ui_element: settings}
        # The below to create my json file when it does not exist
        with open(file_name, "w") as f:
            json.dump(settings_dict, f)
        print(f"saved saved_settings{save_slot}.json")

def load_settings(ui_element, save_slot):
    if os.path.exists(f"saved_settings{save_slot}.json"):
        saved_settings = json.load(open(f"saved_settings{save_slot}.json"))
        print(f"loaded saved_settings{save_slot}.json")
        return saved_settings[ui_element]
