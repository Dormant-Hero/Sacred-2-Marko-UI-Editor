import customtkinter
from PIL import Image
from pathlib import Path
from sacred_ui_functions import *
import tkinter as tk
import sys
from paths import get_base_dir

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

BASE_DIR = get_base_dir()
IMG_PATH = BASE_DIR / "marko_ui_editor_images" / "LOGO S2 Fallen Angel.png"
button_fg_color = "#cebe4a"
button_text_color = "black"
button_hover_color = "#6d5a2b"

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
            number_of_steps=500,
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
        self.title("Sacred 2 UI Customisation (British made application hence no z in customisation. Fight me)")
        self.geometry("1200x600")
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
        # Player portrait button
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

        self.current_frame = frame



    def show_player_portrait_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        portrait_bottom = MyValueSlider(frame, label_text="Player Portrait Vertical Position (0 bottom - 100 top) ")
        portrait_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        portrait_left = MyValueSlider(frame, label_text="Player Portrait Horizontal Position (0 left - 100 right) ")
        portrait_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        portrait_scale = MyScaleSlider(frame, label_text="Player Portrait Size (0 - 5) ")
        portrait_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : player_portrait(bottom=portrait_bottom.get()*5.5, left=portrait_left.get()*11.5, transform_scale=portrait_scale.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame

    def show_minimap_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        minimap_bottom = MyValueSlider(frame, label_text="Minimap Vertical Position (0 bottom - 100 top) ")
        minimap_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        minimap_left = MyValueSlider(frame, label_text="Minimap Horizontal Position (0 left - 100 right) ")
        minimap_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        minimap_scale = MyScaleSlider(frame, label_text="Minimap Size (0 - 5) ")
        minimap_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # def apply_minimap():
        #     slider_val_0_100 = minimap_scale.get()
        #     scale_0_5 = (slider_val_0_100 / 100.0) * 5.0  # linear mapping
        #     minimap(bottom=minimap_bottom.get(), left=minimap_left.get(), transform_scale=scale_0_5)

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : minimap(bottom=minimap_bottom.get(), left=minimap_left.get(), transform_scale=minimap_scale.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame

    def show_taskbar_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        taskbar_bottom = MyValueSlider(frame, label_text="Taskbar Vertical Position (0 bottom - 100 top) ")
        taskbar_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        taskbar_left = MyValueSlider(frame, label_text="Taskbar Horizontal Position (0 left - 100 right) ")
        taskbar_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        taskbar_scale = MyScaleSlider(frame, label_text="Taskbar Size (0 - 5) ")
        taskbar_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : taskbar(bottom=taskbar_bottom.get()*7, left=taskbar_left.get(), transform_scale=taskbar_scale.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame

    def show_taskbar_inventory_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        taskbar_bottom_inv = MyValueSlider(frame, label_text="Taskbar_Inv Vertical Position (0 bottom - 100 top) ")
        taskbar_bottom_inv.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        taskbar_left_inv = MyValueSlider(frame, label_text="Taskbar_Inv Horizontal Position (0 left - 100 right) ")
        taskbar_left_inv.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        taskbar_scale_inv = MyScaleSlider(frame, label_text="Taskbar_Inv Size (0 - 5) ")
        taskbar_scale_inv.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : taskbar_inventory(bottom=taskbar_bottom_inv.get(), left=taskbar_left_inv.get()*0.9, transform_scale=taskbar_scale_inv.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame

    def show_taskbar_combat_arts_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        taskbar_bottom_ca = MyValueSlider(frame, label_text="Taskbar Combat Arts Vertical Position (0 bottom - 100 top) ")
        taskbar_bottom_ca.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        taskbar_left_ca = MyValueSlider(frame, label_text="Taskbar Combat Arts Horizontal Position (0 left - 100 right) ")
        taskbar_left_ca.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        taskbar_scale_ca = MyScaleSlider(frame, label_text="Taskbar Combat Arts Size (0 - 5) ")
        taskbar_scale_ca.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : taskbar_combat_arts(bottom=taskbar_bottom_ca.get(), left=taskbar_left_ca.get()*1, transform_scale=taskbar_scale_ca.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame

    def show_action_slots_left_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        weapons_bottom = MyValueSlider(frame, label_text="Weapons Vertical Position (0 bottom - 100 top) ")
        weapons_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        weapons_left = MyValueSlider(frame, label_text="Weapons Horizontal Position (0 left - 100 right) ")
        weapons_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        weapons_scale = MyScaleSlider(frame, label_text="Weapons Size (0 - 5) ")
        weapons_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : action_slots_left(bottom=weapons_bottom.get()*6, left=weapons_left.get()*1, transform_scale=weapons_scale.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame

    def show_action_slots_right_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        combat_arts_bottom = MyValueSlider(frame, label_text="Combat Arts Vertical Position (0 bottom - 100 top) ")
        combat_arts_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        combat_arts_left = MyValueSlider(frame, label_text="Combat Arts Horizontal Position (0 right - 100 left) ")
        combat_arts_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        combat_arts_scale = MyScaleSlider(frame, label_text="Combat Arts Size (0 - 5) ")
        combat_arts_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : action_slots_right(bottom=combat_arts_bottom.get()*6, right=combat_arts_left.get(), transform_scale=combat_arts_scale.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame

    def show_action_slots_left_inventory_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        weapons_inv_bottom = MyValueSlider(frame, label_text="Weapons Inventory Vertical Position (0 bottom - 100 top) ")
        weapons_inv_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        weapons_inv_left = MyValueSlider(frame, label_text="Weapons Inventory Horizontal Position (0 left - 100 right) ")
        weapons_inv_left.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        weapons_inv_scale = MyScaleSlider(frame, label_text="Weapons Inventory Size (0 - 5) ")
        weapons_inv_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : action_slots_left_inventory(bottom=weapons_inv_bottom.get()-25, left=weapons_inv_left.get(), transform_scale=weapons_inv_scale.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame

    def show_action_slots_right_inventory_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        combat_art_inv_bottom = MyValueSlider(frame, label_text="Combat Art Inventory Vertical Position (0 bottom - 100 top) ")
        combat_art_inv_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        combat_art_inv_right = MyValueSlider(frame, label_text="Combat Art Inventory Horizontal Position (0 right - 100 left) ")
        combat_art_inv_right.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        combat_art_inv_scale = MyScaleSlider(frame, label_text="Combat Art Inventory Size (0 - 5) ")
        combat_art_inv_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : action_slots_right_inventory(bottom=combat_art_inv_bottom.get()-25, right=combat_art_inv_right.get(), transform_scale=combat_art_inv_scale.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame


    def show_action_slots_left_combat_arts_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        weapons_ca_bottom = MyValueSlider(frame, label_text="Weapons Combat Art Screen Vertical Position (0 bottom - 100 top) ")
        weapons_ca_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        weapons_ca_right = MyValueSlider(frame, label_text="Weapons Combat Art Screen Horizontal Position (0 left - 100 right) ")
        weapons_ca_right.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        weapons_ca_right_scale = MyScaleSlider(frame, label_text="Weapons Combat Art Screen Size (0 - 5) ")
        weapons_ca_right_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : action_slots_left_combat_arts(bottom=weapons_ca_bottom.get()-25, left=weapons_ca_right.get(), transform_scale=weapons_ca_right_scale.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame

    def show_action_slots_right_combat_arts_screen(self):
        self.clear_frame()
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")

        combat_arts_ca_bottom = MyValueSlider(frame, label_text="Combat Arts CA Screen Vertical Position (0 bottom - 100 top) ")
        combat_arts_ca_bottom.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        combat_arts_ca_right = MyValueSlider(frame, label_text="Combat Arts CA Screen Horizontal Position (0 right - 100 left) ")
        combat_arts_ca_right.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        combat_arts_ca_scale = MyScaleSlider(frame, label_text="Combat Arts CA Screen Size (0 - 5) ")
        combat_arts_ca_scale.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        apply = MyButton(
            frame,
            text="Apply",
            command=lambda : action_slots_right_combat_arts(bottom=combat_arts_ca_bottom.get()-25, right=combat_arts_ca_right.get(), transform_scale=combat_arts_ca_scale.get())
        )
        apply.grid(row=0, column=1, padx=80, pady=(20, 0), sticky="new", rowspan=1, columnspan=2)

        back_btn = MyButton(frame, text="Back", command=self.show_main_screen)
        back_btn.grid(row=100, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = frame


app = App()
app.mainloop()