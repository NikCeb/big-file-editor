"""Configuration settings for the File Processor application."""

# UI Colors
BG_COLOR = "#f5f5f5"
ACCENT_COLOR = "#4a6ea9"

# File types for file dialog
FILE_TYPES = (
    ("All files", "*.*"),
    ("Text files", "*.txt"),
    ("CSV files", "*.csv")
)

# Window settings
WINDOW_SIZE = "600x600"
PADDING = 20

# Default values
DEFAULT_OUTPUT_DIR = ""  # Set a default output directory if desired