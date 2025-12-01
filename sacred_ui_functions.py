from pathlib import Path
from xml.etree import ElementTree as ET
import cssutils
import sys
from json_functions import *
import logging

cssutils.log.setLevel(logging.CRITICAL)

def get_game_root() -> Path:
    if getattr(sys, "frozen", False):
        # Path to the actual exe on disk: .../Remaster/Marko_Sacred_UI_App/MarkoSacredUI
        exe_path = Path(sys.argv[0]).resolve()
        return exe_path.parent.parent  # .. -> Remaster
    else:
        # Running from source: user_interface.py is in Marko_Sacred_UI_App
        return Path(__file__).resolve().parent.parent  # .. -> Remaster

GAME_ROOT = get_game_root()              # /.../Remaster
UI_ROOT   = GAME_ROOT / "ui"             # /.../Remaster/ui

CHAR_DETAILS_PATH = UI_ROOT / "HUD" / "hud_characterDetails.rml"
MINIMAP_PATH      = UI_ROOT / "HUD" / "hud_Minimap.rml"
TASKBAR_PATH      = UI_ROOT / "HUD" / "hud_taskBarCenter.rml"
ACTION_SLOTS      = UI_ROOT / "HUD" / "hud_taskBarActionSlots.rml"
TABMAP            = UI_ROOT / "HUD" / "hud_Tabmap.rml"

def obtain_css_sheet(file_path):
    with file_path.open(encoding="utf-8") as f:
        file_contents = f.read()
    tree = ET.parse(file_path)
    root = tree.getroot()
    ns = {}
    head = root.find("head", ns)
    style_el = head.find("style", ns)
    css_text = style_el.text or ""
    return  cssutils.parseString(css_text), tree, style_el

def player_portrait(bottom, direction_value, transform_scale):
    function_data = obtain_css_sheet(CHAR_DETAILS_PATH)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".player-portrait-position":
            style = rule.style
            style.setProperty("bottom", f"{bottom-15}%")
            style.setProperty("left", f"{direction_value-5}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(CHAR_DETAILS_PATH, encoding="utf-8", xml_declaration=True)
        elif rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".gaugeHP":
            style = rule.style
            style.setProperty("transform", "scale(1)")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(CHAR_DETAILS_PATH, encoding="utf-8", xml_declaration=True)
        elif rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".gaugeShield":
            style = rule.style
            style.setProperty("transform", "scale(1)")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(CHAR_DETAILS_PATH, encoding="utf-8", xml_declaration=True)
        elif rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".gaugeXP":
            style = rule.style
            style.setProperty("transform", "scale(1)")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(CHAR_DETAILS_PATH, encoding="utf-8", xml_declaration=True)

def minimap(bottom, direction_value, transform_scale):
    function_data = obtain_css_sheet(MINIMAP_PATH)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".minimap-position":
            style = rule.style
            style.setProperty("bottom", f"{bottom-15}%")
            style.setProperty("left", f"{direction_value-6.5}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(MINIMAP_PATH, encoding="utf-8", xml_declaration=True)

def taskbar(bottom, direction_value, transform_scale):
    function_data = obtain_css_sheet(TASKBAR_PATH)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".taskbar":
            style = rule.style
            style.setProperty("bottom", f"{bottom*1.01}%")
            style.setProperty("left", f"{direction_value-20}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(TASKBAR_PATH, encoding="utf-8", xml_declaration=True)

def taskbar_inventory(bottom, direction_value, transform_scale):
    function_data = obtain_css_sheet(TASKBAR_PATH)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".taskbar.inventory":
            style = rule.style
            style.setProperty("bottom", f"{bottom-5}%")
            style.setProperty("left", f"{direction_value-15}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(TASKBAR_PATH, encoding="utf-8", xml_declaration=True)
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".taskbar.inventory-scaled":
            style = rule.style
            style.setProperty("bottom", f"{bottom-5}%")
            style.setProperty("left", f"{direction_value-15}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(TASKBAR_PATH, encoding="utf-8", xml_declaration=True)

def taskbar_combat_arts(bottom, direction_value, transform_scale):
    function_data = obtain_css_sheet(TASKBAR_PATH)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".taskbar.combat-arts":
            style = rule.style
            style.setProperty("bottom", f"{bottom-5}%")
            style.setProperty("left", f"{direction_value-10}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(TASKBAR_PATH, encoding="utf-8", xml_declaration=True)
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".taskbar.combat-arts-scaled":
            style = rule.style
            style.setProperty("bottom", f"{bottom-5}%")
            style.setProperty("left", f"{direction_value-10}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(TASKBAR_PATH, encoding="utf-8", xml_declaration=True)

def action_slots_left(direction_value, bottom, transform_scale):
    function_data = obtain_css_sheet(ACTION_SLOTS)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".action-slot-container-left":
            style = rule.style
            style.setProperty("bottom", f"{bottom*1.01-10}%")
            style.setProperty("left", f"{direction_value-5}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(ACTION_SLOTS, encoding="utf-8", xml_declaration=True)

def action_slots_right(direction_value, bottom, transform_scale):
    function_data = obtain_css_sheet(ACTION_SLOTS)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".action-slot-container-right":
            style = rule.style
            style.setProperty("bottom", f"{bottom*1.01-10}%")
            style.setProperty("right", f"{direction_value-5}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(ACTION_SLOTS, encoding="utf-8", xml_declaration=True)

def action_slots_left_inventory(bottom, direction_value, transform_scale):
    function_data = obtain_css_sheet(ACTION_SLOTS)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".inventory-left":
            style = rule.style
            style.setProperty("bottom", f"{bottom*1.02-20}%")
            style.setProperty("left", f"{direction_value}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(ACTION_SLOTS, encoding="utf-8", xml_declaration=True)

def action_slots_right_inventory(bottom, direction_value, transform_scale):
    function_data = obtain_css_sheet(ACTION_SLOTS)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".inventory-right":
            style = rule.style
            style.setProperty("bottom", f"{bottom*1.02-20}%")
            style.setProperty("right", f"{direction_value-5}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(ACTION_SLOTS, encoding="utf-8", xml_declaration=True)

def action_slots_left_combat_arts(bottom, direction_value, transform_scale):
    function_data = obtain_css_sheet(ACTION_SLOTS)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".combat-arts-left":
            style = rule.style
            style.setProperty("bottom", f"{bottom*1.02-20}%")
            style.setProperty("left", f"{direction_value-5}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(ACTION_SLOTS, encoding="utf-8", xml_declaration=True)

def action_slots_right_combat_arts(bottom, direction_value, transform_scale):
    function_data = obtain_css_sheet(ACTION_SLOTS)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".combat-arts-right":
            style = rule.style
            style.setProperty("bottom", f"{bottom*1.02-20}%")
            style.setProperty("right", f"{direction_value-5}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(ACTION_SLOTS, encoding="utf-8", xml_declaration=True)

def tabmap_hud(direction_value, bottom, transform_scale):
    print(TABMAP)
    function_data = obtain_css_sheet(TABMAP)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == "#tabmap":
            style = rule.style
            style.setProperty("top", f"{bottom*1.05-50}%")
            style.setProperty("left", f"{direction_value*1.05-50}%")
            style.setProperty("transform", f"scale({transform_scale})")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(TABMAP, encoding="utf-8", xml_declaration=True)


# tabmap_hud(left=50, top=10, transform_scale=0.25)

# player_portrait(bottom=0, left=0, transform_scale=0.5)
#
# minimap(70, 85, 1)
#
# # taskbar left is a %
# taskbar(30, 30.5, 1)
#
# action_slots_left(25, 400, 2)
#
# action_slots_right(25, 400, 2)
#
# action_slots_left_inventory(-6.5, 29.55, 1)
#
# action_slots_right_inventory(-6.5, 2.1, 1)

# taskbar_inventory(bottom=5, left=43, transform_scale=1)

# action_slots_left_combat_arts(bottom=-7.7, left=2.65, transform_scale=1)

# action_slots_right_combat_arts(bottom=-6.5, right=29.8, transform_scale=1)

# taskbar_combat_arts(bottom=5, left=16.5, transform_scale=1)


