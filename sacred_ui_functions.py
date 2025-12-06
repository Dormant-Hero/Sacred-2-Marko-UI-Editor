from pathlib import Path
from xml.etree import ElementTree as ET
import cssutils
import sys
from json_functions import *
import logging
from lxml import etree  # in addition to your existing imports
from icecream import ic


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
ALT_TEXT = UI_ROOT / "HUD" / "hud_AltText.rml"
FADING_TEXT = UI_ROOT / "HUD" / "hud_FloatingText.rml"
ITEMS_TOOLTIP = UI_ROOT / "Ingame" / "items_Tooltip.rml"

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

def alt_text_style(font_size, color, font_family):
    function_data = obtain_css_sheet(ALT_TEXT)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".alt-text":
            style = rule.style
            style.setProperty("font-size", f"{font_size}vh")
            style.setProperty("color", f"{color}")
            style.setProperty("font-family", f"{font_family}")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(ALT_TEXT, encoding="utf-8", xml_declaration=True)

def floating_text_font(font_size, font_family, **kwargs):
    outline = kwargs.get("outline", "0")
    outline_color = kwargs.get("outline_color", "black")
    ic(font_size, font_family, outline, outline_color)
    function_data = obtain_css_sheet(FADING_TEXT)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == ".floating-text":
            style = rule.style
            if outline != "0" and outline_color != "black":
                style.setProperty("font-effect", f"outline({outline}dp {outline_color})")
            style.setProperty("font-size", f"{font_size}vh")
            style.setProperty("font-family", f"{font_family}")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(FADING_TEXT, encoding="utf-8", xml_declaration=True)



def add_class_to_tooltip(selector_string, font_size, color, font_family):
    sheet, tree, style_el = obtain_css_sheet(ITEMS_TOOLTIP)  # adjust unpacking order if needed

    rule = None
    for r in sheet:
        if r.type == r.STYLE_RULE and r.selectorText.strip() == selector_string:
            rule = r
            break

    if rule is None:
        # create a new rule with a fresh declaration block
        style = cssutils.css.CSSStyleDeclaration()
        rule = cssutils.css.CSSStyleRule(selectorText=selector_string, style=style)
        sheet.add(rule)  # adds rule at appropriate position in the stylesheet[web:2][web:28]
    else:
        style = rule.style

    # set or override the properties
    style.setProperty("font-size", f"{font_size}vh")
    style.setProperty("color", f"{color}")
    style.setProperty("font-family", f"{font_family}")
    print(f"{rule.selectorText} just happened")

    # serialize and write back
    css = sheet.cssText.decode("utf-8")
    css = css.replace("translatex(", "translateX(")
    style_el.text = css
    tree.write(ITEMS_TOOLTIP, encoding="utf-8", xml_declaration=True)

def item_tooltip_stats(font_size, color, font_family):
    selector_text1 = ".stat-name"
    selector_text2 = ".stat-value"
    add_class_to_tooltip(selector_text1, font_size, color, font_family)
    add_class_to_tooltip(selector_text2, font_size, color, font_family)

# just the value of armour or whatever primary value is for any given item
def items_tooltip_primary_value_stat(font_size, color, font_family):
    selector_text1 = ".primary-value-text"
    add_class_to_tooltip(selector_text1, font_size, color, font_family)

def mastery_required_for_bonus_text(font_size, color, font_family):
    selector_text1 = ".mastery-text"
    add_class_to_tooltip(selector_text1, font_size, color, font_family)

def amend_body_gold_style(file_path, font_size, color, font_family):
    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.parse(str(file_path), parser)
    root = tree.getroot()

    # find <div class="price">
    price_divs = root.xpath("//div[@class='price']")
    for price_div in price_divs:
        # children of .price that have a style attribute
        for child in price_div.xpath("./*[@style]"):
            style_attr = child.get("style")
            if not style_attr:
                continue
            style = cssutils.css.CSSStyleDeclaration(cssText=style_attr)
            style.setProperty("font-size", f"{font_size}vh")
            style.setProperty("color", f"{color}")
            style.setProperty("font-family", f"{font_family}")

            child.set("style", style.cssText)

    tree.write(str(file_path), encoding="utf-8", xml_declaration=True, pretty_print=True)

def tooltip_item_name(font_size, color, font_family):
    function_data = obtain_css_sheet(ITEMS_TOOLTIP)
    sheet = function_data[0]
    style_el = function_data[2]
    tree = function_data[1]
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText.strip() == "#tooltip-item-name":
            style = rule.style
            style.setProperty("font-size", f"{font_size}vh")
            style.setProperty("color", f"{color}")
            style.setProperty("font-family", f"{font_family}")
            (print(f"{rule.selectorText} just happened"))
            css = sheet.cssText.decode("utf-8")
            css = css.replace("translatex(", "translateX(")
            style_el.text = css
            tree.write(ITEMS_TOOLTIP, encoding="utf-8", xml_declaration=True)

# tooltip_item_name(3, "red", "inria sans")

# amend_body_gold_style(ITEMS_TOOLTIP, font_size=4, color="white", font_family="OptimusPrinceps")

# items_tooltip_primary_value_stat(1, font_family="Inria Sans", color="red")

# fading_text_font(13, "blue", font_family="OptimusPrinceps", outline=10, outline_color="red")

# alt_text_font(font_size=8, color="red", font_family='"Inria Sans"')


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


