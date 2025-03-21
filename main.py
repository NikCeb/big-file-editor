"""
File: main.py
Author: Nikolai Ceballos
Date: 2025-03-20
Description: Calls the GUI.
"""

import tkinter as tk
from app_gui import FileProcessorGUI

def main():
    """Application entry point."""
    root = tk.Tk()
    app = FileProcessorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()