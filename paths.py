from pathlib import Path
import sys

def get_base_dir() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        # Running as PyInstaller bundle
        return Path(sys._MEIPASS)
    else:
        # Running from source: directory that contains user_interface.py
        return Path(__file__).parent