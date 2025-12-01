import customtkinter
from PIL import Image
from pathlib import Path
from sacred_ui_functions import *
import tkinter as tk
import sys
from paths import get_parent_dir

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

BASE_DIR = get_parent_dir()
IMG_PATH = BASE_DIR / "marko_ui_editor_images" / "LOGO S2 Fallen Angel.png"
button_fg_color = "#cebe4a"
button_text_color = "black"
button_hover_color = "#6d5a2b"


def right_screen(self, ui_element, bottom, direction, direction_value, scale, load_settings_func,
                 load_setting_slot_func):
    right_frame = customtkinter.CTkFrame(self)
    right_frame.grid(row=0, column=1, sticky="nsew")
    print(globals()[ui_element])
    print(scale.get())
    def what_do_i_get():
        print(bottom.get())
    apply = MyButton(
        right_frame,
        text="Apply",
        #below globals is pulling functions from sacred_ui_functions.py
        command=lambda: [what_do_i_get(),globals()[ui_element](bottom=bottom.get(), direction_value=direction_value.get(),
                                                   transform_scale=scale.get()),
                         save_settings_last_applied(ui_element=f"{ui_element}",
                                                    settings={"bottom": f"{bottom.get()}",
                                                              f"{direction}": f"{direction_value.get()}",
                                                              "scale": f"{scale.get()}", }),
                         load_settings_last_applied(ui_element=f"{ui_element}", )
                         ]
    )

    apply.grid(row=0, column=3, padx=2, pady=(20, 0), sticky="new", columnspan=1)

    load_applied_btn = MyButton(
        right_frame,
        text="Load Last Applied Settings",
        command=lambda: load_settings_func())
    load_applied_btn.grid(row=0, column=4, padx=2, pady=(20, 0), sticky="ne", columnspan=1)

    save_slot_1_btn = MyButton(right_frame,
                               text="Save Slot 1",
                               command=lambda: save_settings(
                                   ui_element=f"{ui_element}",
                                   save_slot=1,
                                   settings={"bottom": f"{round(bottom.get(), 2)}",
                                             "left": f"{round(direction_value.get(), 2)}",
                                             "scale": f"{round(scale.get(), 2)}"}
                               ))
    save_slot_1_btn.grid(row=1, column=3, padx=2, pady=(8, 0), sticky="new", rowspan=1, columnspan=1)

    save_slot_2_btn = MyButton(right_frame,
                               text="Save Slot 2",
                               command=lambda: save_settings(
                                   ui_element=f"{ui_element}",
                                   save_slot=2,
                                   settings={"bottom": f"{round(bottom.get(), 2)}",
                                             "left": f"{round(direction_value.get(), 2)}",
                                             "scale": f"{round(scale.get(), 2)}"}
                               ))
    save_slot_2_btn.grid(row=2, column=3, padx=2, pady=(8, 0), sticky="new", columnspan=1)

    save_slot_3_btn = MyButton(right_frame,
                               text="Save Slot 3",
                               command=lambda: save_settings(
                                   ui_element=f"{ui_element}",
                                   save_slot=3,
                                   settings={"bottom": f"{round(bottom.get(), 2)}",
                                             "left": f"{round(direction_value.get(), 2)}",
                                             "scale": f"{round(scale.get(), 2)}"}
                               ))
    save_slot_3_btn.grid(row=3, column=3, padx=2, pady=(8, 0), sticky="new", columnspan=1)

    load_slot_1_btn = MyButton(right_frame,
                               text="Load Slot 1",
                               command=lambda: load_setting_slot_func(1)
                               )
    load_slot_1_btn.grid(row=1, column=4, padx=2, pady=(8, 0), sticky="new", columnspan=1)

    load_slot_2_btn = MyButton(right_frame,
                               text="Load Slot 2",
                               command=lambda: load_setting_slot_func(2)
                               )
    load_slot_2_btn.grid(row=2, column=4, padx=2, pady=(8, 0), sticky="new", columnspan=1)

    load_slot_3_btn = MyButton(right_frame,
                               text="Load Slot 3",
                               command=lambda: load_setting_slot_func(3)
                               )
    load_slot_3_btn.grid(row=3, column=4, padx=2, pady=(8, 0), sticky="new", columnspan=1)
    self.current_frame = right_frame

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class MyButton(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        defaults = dict(
            fg_color=button_fg_color,
            text_color=button_text_color,
            hover_color=button_hover_color
        )
        defaults.update(kwargs)
        super().__init__(master, **defaults)

class MySliders(customtkinter.CTkSlider):
    def __init__(self, master, **kwargs):
        defaults = dict(
            from_=0,
            to=100,
            number_of_steps=1000,
        )
        defaults.update(kwargs)
        super().__init__(master, **defaults)

class MyValueSlider(customtkinter.CTkFrame):
    def __init__(self, master, label_text="Value", **kwargs):
        super().__init__(master, **kwargs)

        self.var = tk.DoubleVar(master=self, value=0.0)      # raw float
        self.display_var = tk.StringVar(master=self, value="0.00")  # formatted text

        self.text_label = MyLabel(self, text=label_text)
        self.text_label.grid(row=0, column=0, padx=(0, 5), sticky="w")

        self.slider = MySliders(self, variable=self.var, command=self._slider_changed)
        self.slider.grid(row=0, column=1, sticky="ew")

        self.value_label = MyLabel(self, textvariable=self.display_var)
        self.value_label.grid(row=0, column=2, padx=(5, 0), sticky="e")

        self.grid_columnconfigure(1, weight=1)

    def set(self, value: float) -> None:
        self.slider.set(value)
        self.display_var.set(f"{round(value, 2)}")

    def _slider_changed(self, value):
        # value comes in as a string; format to 2 dp
        self.display_var.set(f"{float(value):.2f}")

    def get(self):
        return self.var.get()

    def _on_slide_proxy(self, value):
        # called by CTkSlider, forward to overridable hook
        self.on_slide(value)

    def on_slide(self, value):
        # default behavior; override in subclasses if you want
        print(float(value))
        return float(value)

class MyScaleSlider(customtkinter.CTkFrame):
    def __init__(self, master, label_text="Value", **kwargs):
        super().__init__(master, **kwargs)

        self.var = tk.DoubleVar(master=self, value=1.0)      # raw float
        self.display_var = tk.StringVar(master=self, value="1.00")  # formatted text

        self.text_label = MyLabel(self, text=label_text)
        self.text_label.grid(row=0, column=0, padx=(0, 5), sticky="w")

        self.slider = MySliders(self, variable=self.var, command=self._slider_changed, from_=0, to=5)
        self.slider.grid(row=0, column=1, sticky="ew")

        self.value_label = MyLabel(self, textvariable=self.display_var)
        self.value_label.grid(row=0, column=2, padx=(5, 0), sticky="e")

        self.grid_columnconfigure(1, weight=1)

    def set(self, value: float) -> None:
        self.slider.set(value)
        self.display_var.set(f"{round(value, 2)}")

    def _slider_changed(self, value):
        # value comes in as a string; format to 2 dp
        self.display_var.set(f"{float(value):.2f}")

    def get(self):
        return self.var.get()

    def _on_slide_proxy(self, value):
        # called by CTkSlider, forward to overridable hook
        self.on_slide(value)

    def on_slide(self, value):
        # default behavior; override in subclasses if you want
        print(float(value))
        return float(value)

class MyLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        defaults = dict(
            text_color="white",
            anchor="w",
        )
        defaults.update(kwargs)
        super().__init__(master, **defaults)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sacred 2 UI Editor")
        self.geometry("1700x600") #allows for the 0.1 increments when it is this wide hopefully fine.
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.current_frame = None
        self.show_main_screen()

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

    def show_main_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_columnconfigure(1, weight=1)  # button part 1
        frame.grid_columnconfigure(2, weight=1)  # button part 2
        img = Image.open(IMG_PATH)
        ctk_image = customtkinter.CTkImage(light_image=img, dark_image=img, size=(400, 500))
        image_label = customtkinter.CTkLabel(frame, image=ctk_image, text="")
        image_label.image = ctk_image              # keep reference
        image_label.grid(row=0, column=0, rowspan=100, padx=10, pady=10, sticky="w")

        button_player_portrait = MyButton(frame, text="Player Portrait",
                          command=self.show_player_portrait_screen)
        button_player_portrait.grid(row=0, column=1, padx=40, pady=(85, 0), sticky="new", rowspan=1, columnspan=2)
        button_minimap = MyButton(frame, text="Minimap",
                          command=self.show_minimap_screen)
        button_minimap.grid(row=1, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_taskbar = MyButton(frame, text="Taskbar",
                          command=self.show_taskbar_screen)
        button_taskbar.grid(row=2, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_left_action_slots = MyButton(frame, text="Weapons HUD", command=self.show_action_slots_left_screen)
        button_left_action_slots.grid(row=3, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_right_action_slots = MyButton(frame, text="Combat Arts HUD", command=self.show_action_slots_right_screen)
        button_right_action_slots.grid(row=4, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_taskbar_inv = MyButton(frame, text="Taskbar (Inventory Screen)", command=self.show_taskbar_inventory_screen)
        button_taskbar_inv.grid(row=5, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_taskbar_inv = MyButton(frame, text="Taskbar (Combat Art Screen)", command=self.show_taskbar_combat_arts_screen)
        button_taskbar_inv.grid(row=6, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_left_action_slots_inv = MyButton(frame, text="Weapons (Inventory Screen)", command=self.show_action_slots_left_inventory_screen)
        button_left_action_slots_inv.grid(row=7, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_right_action_slots_inv = MyButton(frame, text="Combat Arts (Inventory Screen)", command=self.show_action_slots_right_inventory_screen)
        button_right_action_slots_inv.grid(row=8, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_left_action_slots_ca = MyButton(frame, text="Weapons (Combat Art Screen)", command=self.show_action_slots_left_combat_arts_screen)
        button_left_action_slots_ca.grid(row=9, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_right_action_slots_ca = MyButton(frame, text="Combat Arts (Combat Art Screen)", command=self.show_action_slots_right_combat_arts_screen)
        button_right_action_slots_ca.grid(row=10, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        button_tabmap_hud = MyButton(frame, text="Tabmap", command=self.show_tabmap_screen)
        button_tabmap_hud.grid(row=11, column=1, padx=40, pady=(5, 0), sticky="new", rowspan=1, columnspan=2)

        self.current_frame = frame

#note to self. Eventually replace right frame with a class or provide a right frame for its content. Time to learn what I should be doin gthe right away.
    def show_player_portrait_screen(self):
        self.clear_frame()
        ui_element = "player_portrait"
        left_frame = customtkinter.CTkFrame(self)

        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)


        portrait_bottom = MyValueSlider(left_frame, label_text="Player Portrait Vertical Position (0 bottom - 100 top) ")
        portrait_bottom.grid(row=0, column=0, padx=20, pady=(20, 8), sticky="ew", columnspan=2)

        portrait_left = MyValueSlider(left_frame, label_text="Player Portrait Horizontal Position (0 left - 100 right) ")
        portrait_left.grid(row=1, column=0, padx=20, pady=(0, 8), sticky="ew", columnspan=2)

        portrait_scale = MyScaleSlider(left_frame, label_text="Player Portrait Size (0 - 5) ")
        portrait_scale.grid(row=2, column=0, padx=20, pady=(0, 8), sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=4, column=0, padx=20, pady=400, sticky="w")

        def load_settings_applied():
            values = load_settings_last_applied(ui_element="player_portrait")
            portrait_bottom.set(float(values["bottom"]))
            portrait_left.set(float(values["left"]))
            portrait_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element="player_portrait", save_slot=save_slot)
            portrait_bottom.set(float(values["bottom"]))
            portrait_left.set(float(values["left"]))
            portrait_scale.set(float(values["scale"]))
            self.current_frame = left_frame


        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=portrait_bottom, direction="left",
                     direction_value=portrait_left, scale=portrait_scale, load_settings_func=load_settings_applied, load_setting_slot_func=load_setting_slot)

    def show_minimap_screen(self):
        ui_element = "minimap"
        self.clear_frame()
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)
        right_frame = customtkinter.CTkFrame(self)
        right_frame.grid(row=0, column=1, sticky="nsew")

        minimap_bottom = MyValueSlider(left_frame, label_text="Minimap Vertical Position (0 bottom - 100 top) ")
        minimap_bottom.grid(row=0, column=0, padx=20, pady=(20,0), sticky="ew", columnspan=2)

        minimap_left = MyValueSlider(left_frame, label_text="Minimap Horizontal Position (0 left - 100 right) ")
        minimap_left.grid(row=1, column=0, padx=20, pady=(8, 0), sticky="ew", columnspan=2)

        minimap_scale = MyScaleSlider(left_frame, label_text="Minimap Size (0 - 5) ")
        minimap_scale.grid(row=2, column=0, padx=20, pady=(8,0), sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=4, column=0, padx=20, pady=400, sticky="w")

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element,)
            minimap_bottom.set(float(values["bottom"]))
            minimap_left.set(float(values["left"]))
            minimap_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            minimap_bottom.set(float(values["bottom"]))
            minimap_left.set(float(values["left"]))
            minimap_scale.set(float(values["scale"]))
            self.current_frame = left_frame


        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=minimap_bottom, direction="left",
                     direction_value=minimap_left, scale=minimap_scale, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

    def show_taskbar_screen(self):
        self.clear_frame()
        ui_element = "taskbar"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)
        right_frame = customtkinter.CTkFrame(self)
        right_frame.grid(row=0, column=1, sticky="nsew")

        taskbar_bottom = MyValueSlider(left_frame, label_text="Taskbar Vertical Position (0 bottom - 100 top) ")
        taskbar_bottom.grid(row=0, column=0, padx=20, pady=(20,0), sticky="ew", columnspan=2)

        taskbar_left = MyValueSlider(left_frame, label_text="Taskbar Horizontal Position (0 left - 100 right) ")
        taskbar_left.grid(row=1, column=0, padx=20, pady=(8,0), sticky="ew", columnspan=2)

        taskbar_scale = MyScaleSlider(left_frame, label_text="Taskbar Size (0 - 5) ")
        taskbar_scale.grid(row=2, column=0, padx=20, pady=(8,0), sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=300, sticky="w")

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            taskbar_bottom.set(float(values["bottom"]))
            taskbar_left.set(float(values["left"]))
            taskbar_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            taskbar_bottom.set(float(values["bottom"]))
            taskbar_left.set(float(values["left"]))
            taskbar_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=taskbar_bottom, direction="left",
                     direction_value=taskbar_left, scale=taskbar_scale, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

    def show_taskbar_inventory_screen(self):
        self.clear_frame()
        ui_element = "taskbar_inventory"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)

        taskbar_bottom_inv = MyValueSlider(left_frame, label_text="Taskbar_Inv Vertical Position (0 bottom - 100 top) ")
        taskbar_bottom_inv.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        taskbar_left_inv = MyValueSlider(left_frame, label_text="Taskbar_Inv Horizontal Position (0 left - 100 right) ")
        taskbar_left_inv.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        taskbar_scale_inv = MyScaleSlider(left_frame, label_text="Taskbar_Inv Size (0 - 5) ")
        taskbar_scale_inv.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            taskbar_bottom_inv.set(float(values["bottom"]))
            taskbar_left_inv.set(float(values["left"]))
            taskbar_scale_inv.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            taskbar_bottom_inv.set(float(values["bottom"]))
            taskbar_left_inv.set(float(values["left"]))
            taskbar_scale_inv.set(float(values["scale"]))
            self.current_frame = left_frame

        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=taskbar_bottom_inv, direction="left",
                     direction_value=taskbar_left_inv, scale=taskbar_scale_inv, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

    def show_taskbar_combat_arts_screen(self):
        self.clear_frame()
        ui_element = "taskbar_combat_arts"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)

        taskbar_bottom_ca = MyValueSlider(left_frame, label_text="Taskbar Combat Arts Vertical Position (0 bottom - 100 top) ")
        taskbar_bottom_ca.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        taskbar_left_ca = MyValueSlider(left_frame, label_text="Taskbar Combat Arts Horizontal Position (0 left - 100 right) ")
        taskbar_left_ca.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        taskbar_scale_ca = MyScaleSlider(left_frame, label_text="Taskbar Combat Arts Size (0 - 5) ")
        taskbar_scale_ca.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = left_frame

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            taskbar_bottom_ca.set(float(values["bottom"]))
            taskbar_left_ca.set(float(values["left"]))
            taskbar_scale_ca.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            taskbar_bottom_ca.set(float(values["bottom"]))
            taskbar_left_ca.set(float(values["left"]))
            taskbar_scale_ca.set(float(values["scale"]))
            self.current_frame = left_frame

        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=taskbar_bottom_ca, direction="left",
                     direction_value=taskbar_left_ca, scale=taskbar_scale_ca, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

    def show_action_slots_left_screen(self):
        self.clear_frame()
        ui_element = "action_slots_left"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)

        weapons_bottom = MyValueSlider(left_frame, label_text="Weapons Vertical Position (0 bottom - 100 top) ")
        weapons_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        weapons_left = MyValueSlider(left_frame, label_text="Weapons Horizontal Position (0 left - 100 right) ")
        weapons_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        weapons_scale = MyScaleSlider(left_frame, label_text="Weapons Size (0 - 5) ")
        weapons_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = left_frame

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            weapons_bottom.set(float(values["bottom"]))
            weapons_left.set(float(values["left"]))
            weapons_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            weapons_bottom.set(float(values["bottom"]))
            weapons_left.set(float(values["left"]))
            weapons_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=weapons_bottom, direction="left",
                     direction_value=weapons_left, scale=weapons_scale, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

    def show_action_slots_right_screen(self):
        self.clear_frame()
        ui_element = "action_slots_right"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)

        combat_arts_bottom = MyValueSlider(left_frame, label_text="Combat Arts Vertical Position (0 bottom - 100 top) ")
        combat_arts_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        combat_arts_left = MyValueSlider(left_frame, label_text="Combat Arts Horizontal Position (0 right - 100 left) ")
        combat_arts_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        combat_arts_scale = MyScaleSlider(left_frame, label_text="Combat Arts Size (0 - 5) ")
        combat_arts_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = left_frame

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            combat_arts_bottom.set(float(values["bottom"]))
            combat_arts_left.set(float(values["left"]))
            combat_arts_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            combat_arts_bottom.set(float(values["bottom"]))
            combat_arts_left.set(float(values["left"]))
            combat_arts_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=combat_arts_bottom, direction="left",
                     direction_value=combat_arts_left, scale=combat_arts_scale, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

    def show_action_slots_left_inventory_screen(self):
        self.clear_frame()
        ui_element = "action_slots_left_inventory"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)

        weapons_inv_bottom = MyValueSlider(left_frame, label_text="Weapons Inventory Vertical Position (0 bottom - 100 top) ")
        weapons_inv_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        weapons_inv_left = MyValueSlider(left_frame, label_text="Weapons Inventory Horizontal Position (0 left - 100 right) ")
        weapons_inv_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        weapons_inv_scale = MyScaleSlider(left_frame, label_text="Weapons Inventory Size (0 - 5) ")
        weapons_inv_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = left_frame

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            weapons_inv_bottom.set(float(values["bottom"]))
            weapons_inv_left.set(float(values["left"]))
            weapons_inv_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            weapons_inv_bottom.set(float(values["bottom"]))
            weapons_inv_left.set(float(values["left"]))
            weapons_inv_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=weapons_inv_bottom, direction="left",
                     direction_value=weapons_inv_left, scale=weapons_inv_scale, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

    def show_action_slots_right_inventory_screen(self):
        self.clear_frame()
        ui_element = "action_slots_right_inventory"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)

        combat_art_inv_bottom = MyValueSlider(left_frame, label_text="Combat Art Inventory Vertical Position (0 bottom - 100 top) ")
        combat_art_inv_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        combat_art_inv_right = MyValueSlider(left_frame, label_text="Combat Art Inventory Horizontal Position (0 right - 100 left) ")
        combat_art_inv_right.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        combat_art_inv_scale = MyScaleSlider(left_frame, label_text="Combat Art Inventory Size (0 - 5) ")
        combat_art_inv_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            combat_art_inv_bottom.set(float(values["bottom"]))
            combat_art_inv_right.set(float(values["right"]))
            combat_art_inv_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            combat_art_inv_bottom.set(float(values["bottom"]))
            combat_art_inv_right.set(float(values["right"]))
            combat_art_inv_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=combat_art_inv_bottom, direction="right",
                     direction_value=combat_art_inv_right, scale=combat_art_inv_scale, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)



    def show_action_slots_left_combat_arts_screen(self):
        self.clear_frame()
        ui_element ="action_slots_left_combat_arts"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)

        weapons_ca_bottom = MyValueSlider(left_frame, label_text="Weapons Combat Art Screen Vertical Position (0 bottom - 100 top) ")
        weapons_ca_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        weapons_ca_right = MyValueSlider(left_frame, label_text="Weapons Combat Art Screen Horizontal Position (0 left - 100 right) ")
        weapons_ca_right.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        weapons_ca_scale = MyScaleSlider(left_frame, label_text="Weapons Combat Art Screen Size (0 - 5) ")
        weapons_ca_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = left_frame

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            weapons_ca_bottom.set(float(values["bottom"]))
            weapons_ca_right.set(float(values["right"]))
            weapons_ca_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            weapons_ca_bottom.set(float(values["bottom"]))
            weapons_ca_right.set(float(values["right"]))
            weapons_ca_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=weapons_ca_bottom, direction="right",
                     direction_value=weapons_ca_right, scale=weapons_ca_scale, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

    def show_action_slots_right_combat_arts_screen(self):
        self.clear_frame()
        ui_element = "action_slots_right_combat_arts"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)

        combat_arts_ca_bottom = MyValueSlider(left_frame, label_text="Combat Arts CA Screen Vertical Position (0 bottom - 100 top) ")
        combat_arts_ca_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        combat_arts_ca_right = MyValueSlider(left_frame, label_text="Combat Arts CA Screen Horizontal Position (0 right - 100 left) ")
        combat_arts_ca_right.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        combat_arts_ca_scale = MyScaleSlider(left_frame, label_text="Combat Arts CA Screen Size (0 - 5) ")
        combat_arts_ca_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = left_frame

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            combat_arts_ca_bottom.set(float(values["bottom"]))
            combat_arts_ca_right.set(float(values["right"]))
            combat_arts_ca_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            combat_arts_ca_bottom.set(float(values["bottom"]))
            combat_arts_ca_right.set(float(values["right"]))
            combat_arts_ca_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=combat_arts_ca_bottom, direction="right",
                     direction_value=combat_arts_ca_right, scale=combat_arts_ca_scale, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

    def show_tabmap_screen(self):
        self.clear_frame()
        ui_element = "tabmap_hud"
        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.grid_columnconfigure(1, weight=1)

        tabmap_bottom = MyValueSlider(left_frame, label_text="Tabmap Vertical Position (0 top - 100 bottom) ")
        tabmap_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        tabmap_left = MyValueSlider(left_frame, label_text="Tabmap Horizontal Position (0 left - 100 right) ")
        tabmap_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        tabmap_scale = MyScaleSlider(left_frame, label_text="Tabmap Size (0 - 5) ")
        tabmap_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        back_btn = MyButton(left_frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = left_frame

        def load_settings_applied():
            values = load_settings_last_applied(ui_element=ui_element)
            tabmap_bottom.set(float(values["bottom"]))
            tabmap_left.set(float(values["left"]))
            tabmap_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        def load_setting_slot(save_slot):
            values = load_settings(ui_element=ui_element, save_slot=save_slot)
            tabmap_bottom.set(float(values["bottom"]))
            tabmap_left.set(float(values["left"]))
            tabmap_scale.set(float(values["scale"]))
            self.current_frame = left_frame

        right_screen(self, ui_element=ui_element, bottom=tabmap_bottom, direction="left",
                     direction_value=tabmap_left, scale=tabmap_scale, load_settings_func=load_settings_applied,
                     load_setting_slot_func=load_setting_slot)

app = App()
app.mainloop()