"""
File: main.py
Author: Nikolai Ceballos
Date: 2025-03-23
Description: Handles the logic for updating specific lines in the GUI based on user input and saving the modified file to a chosen location..
"""

import os
import tkinter as tk
from tkinter import  messagebox

class FileProcessor:
    """Handles file processing tasks."""
    def __init__(self):  # No arguments needed
        pass  

    
    def process_file(self, output_location, line_name, value, file_path):
        """Process a single file and update its contents."""
        to_modified_file_path = file_path

        # Read the modified file
        with open(to_modified_file_path, "rb") as file:
            data = file.read()

        # Convert binary to text
        try:
            text_data = data.decode("utf-8")
        except UnicodeDecodeError:
            text_data = data.decode("latin-1")

        # Update the specific line again (900.0 -> 600.0)
        updated_text = text_data.replace(line_name, value)

        # Convert back to binary and save the modified file again
        updated_binary_data = updated_text.encode("latin-1")

        base_name, ext = os.path.splitext(os.path.basename(file_path))

        # Save the new modified file
        final_modified_file_path = os.path.join(output_location, f"{base_name}_modified{ext}")

        root = tk.Tk()
        root.withdraw()  # Hide the main window
    
        count = 0
        if os.path.exists(final_modified_file_path):
            user_response = messagebox.askyesno("File Exists", f"File {final_modified_file_path} already exists. \n Do you want to replace it? No will save the file with a different name.")
            # User wants to overwrite the file
            if not user_response:
                count = 0
            # User wants to keep file with a different name
            while os.path.exists(final_modified_file_path):
                final_modified_file_path = os.path.join(output_location, f"{base_name}_modified_{count}{ext}")
                count += 1

        root.destroy()  # Close the root window

        # Save the new modified file
        with open(final_modified_file_path, "wb") as file:
            file.write(updated_binary_data)
        
        # Return the final modified file path
        return final_modified_file_path

