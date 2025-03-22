"""
File: main.py
Author: Nikolai Ceballos
Date: 2025-03-20
Description: Gets the file location, file to be changed, values, and line to be changed .
"""

import tkinter as tk
from tkinter import filedialog, ttk
import os
from config import FILE_TYPES, WINDOW_SIZE
from file_processor import FileProcessor

class FileProcessorGUI:
    """A simple GUI application for processing files."""

    def __init__(self, root):
        """Initialize the application."""
        # Configure root window
        
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title(".Big File Updater")
        self.root.geometry(WINDOW_SIZE)  # Increased height for new inputs
        self.root.resizable(True, True)
        self.root.configure(padx=15, pady=15, bg="#f0f0f0")
        
        # Initialize variables
        self.input_file_path = tk.StringVar()
        self.input_dir_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.line_name = tk.StringVar()
        self.value = tk.StringVar()
        self.processor = FileProcessor()

        
        # Create UI elements
        self.create_ui()
    
    def on_closing(self):
        """Handle the window close event."""
        self.root.destroy()
        self.root.quit()

    def create_ui(self):
        """Create the user interface."""
        # Main title
        title_label = tk.Label(
            self.root,
            text="File Processor",
            font=("Helvetica", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=(0, 15))
        
        # Create frames
        self.create_input_frame()
        self.create_output_frame()
        self.create_options_frame()  # New frame for LineName/Option and Value
        self.create_action_frame()
        self.create_status_frame()
    
    def create_input_frame(self):
        """Create the input section for file/directory selection."""
        input_frame = tk.LabelFrame(
            self.root,
            text="Input Selection",
            padx=10,
            pady=10,
            bg="#f0f0f0"
        )
        input_frame.pack(fill="x", padx=5, pady=5)
        
        # File selection row
        file_frame = tk.Frame(input_frame, bg="#f0f0f0")
        file_frame.pack(fill="x", pady=5)
        
        file_label = tk.Label(
            file_frame,
            text="Select File:",
            width=10,
            anchor="w",
            bg="#f0f0f0"
        )
        file_label.pack(side="left")
        
        file_entry = tk.Entry(
            file_frame,
            textvariable=self.input_file_path,
            width=40
        )
        file_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        file_button = tk.Button(
            file_frame,
            text="Browse",
            command=self.browse_file,
            bg="#4a86e8",
            fg="white",
            padx=10
        )
        file_button.pack(side="left", padx=5)
    
    
    def create_output_frame(self):
        """Create the output location selection section."""
        output_frame = tk.LabelFrame(
            self.root,
            text="Output Location",
            padx=10,
            pady=10,
            bg="#f0f0f0"
        )
        output_frame.pack(fill="x", padx=5, pady=10)
        
        output_row = tk.Frame(output_frame, bg="#f0f0f0")
        output_row.pack(fill="x", pady=5)
        
        output_label = tk.Label(
            output_row,
            text="Save To:",
            width=10,
            anchor="w",
            bg="#f0f0f0"
        )
        output_label.pack(side="left")
        
        output_entry = tk.Entry(
            output_row,
            textvariable=self.output_path,
            width=40
        )
        output_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        output_button = tk.Button(
            output_row,
            text="Browse",
            command=self.browse_output,
            bg="#4a86e8",
            fg="white",
            padx=10
        )
        output_button.pack(side="left", padx=5)
    
    def create_options_frame(self):
        """Create the options section for LineName/Option and Value inputs."""
        options_frame = tk.LabelFrame(
            self.root,
            text="Processing Options",
            padx=10,
            pady=10,
            bg="#f0f0f0"
        )
        options_frame.pack(fill="x", padx=5, pady=10)
        
        # LineName/Option row
        line_name_frame = tk.Frame(options_frame, bg="#f0f0f0")
        line_name_frame.pack(fill="x", pady=5)
        
        line_name_label = tk.Label(
            line_name_frame,
            text="LineName/Option:",
            width=15,
            anchor="w",
            bg="#f0f0f0"
        )
        line_name_label.pack(side="left")
        
        line_name_entry = tk.Entry(
            line_name_frame,
            textvariable=self.line_name,
            width=40
        )
        line_name_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        # Value row
        value_frame = tk.Frame(options_frame, bg="#f0f0f0")
        value_frame.pack(fill="x", pady=5)
        
        value_label = tk.Label(
            value_frame,
            text="Value:",
            width=15,
            anchor="w",
            bg="#f0f0f0"
        )
        value_label.pack(side="left")
        
        value_entry = tk.Entry(
            value_frame,
            textvariable=self.value,
            width=40
        )
        value_entry.pack(side="left", padx=5, fill="x", expand=True)
    
    def create_action_frame(self):
        """Create the action buttons section."""
        action_frame = tk.Frame(self.root, bg="#f0f0f0")
        action_frame.pack(pady=10)
        
        process_button = tk.Button(
            action_frame,
            text="Process Files",
            command=self.process_files,
            bg="#4caf50",
            fg="white",
            font=("Helvetica", 11, "bold"),
            padx=15,
            pady=5
        )
        process_button.pack(side="left", padx=5)
        
        clear_button = tk.Button(
            action_frame,
            text="Clear All",
            command=self.clear_all,
            bg="#f44336",
            fg="white",
            font=("Helvetica", 11),
            padx=15,
            pady=5
        )
        clear_button.pack(side="left", padx=5)
    
    def create_status_frame(self):
        """Create the status display section."""
        status_frame = tk.LabelFrame(
            self.root,
            text="Status",
            padx=10,
            pady=10,
            bg="#f0f0f0"
        )
        status_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            status_frame,
            orient="horizontal",
            length=100,
            mode="determinate"
        )
        self.progress.pack(fill="x", pady=5)
        
        # Status text area
        self.status_text = tk.Text(
            status_frame,
            height=5,
            width=40,
            wrap="word",
            bg="white"
        )
        self.status_text.pack(fill="both", expand=True)
        
        # Add scrollbar
        scrollbar = tk.Scrollbar(self.status_text)
        scrollbar.pack(side="right", fill="y")
        self.status_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.status_text.yview)
        
        # Initial status message
        self.update_status("Ready to process files.")
        self.status_text.config(state=tk.DISABLED)
    
    def browse_file(self):
        """Open file browser dialog to select a file."""
        filename = filedialog.askopenfilename(
            title="Select a .big file",
            filetypes=FILE_TYPES
        )
        if filename:
            self.input_file_path.set(filename)
            self.update_status(f"Selected file: {os.path.basename(filename)}")
    
    def browse_directory(self):
        """Open directory browser dialog to select a folder."""
        directory = filedialog.askdirectory(title="Select a folder")
        if directory:
            self.input_dir_path.set(directory)
            self.update_status(f"Selected directory: {directory}")
    
    def browse_output(self):
        """Open directory browser dialog to select output location."""
        directory = filedialog.askdirectory(title="Select output location")
        if directory:
            self.output_path.set(directory)
            self.update_status(f"Output location set to: {directory}")
    
    def update_status(self, message):
        """Update the status text area with a new message."""
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)
    
    def clear_all(self):
        """Clear all input fields and reset status."""
        self.input_file_path.set("")
        self.input_dir_path.set("")
        self.output_path.set("")
        self.line_name.set("")
        self.value.set("")
        self.progress["value"] = 0
        self.status_text.delete(1.0, tk.END)
        self.update_status("All fields cleared.")
    
    def process_files(self):
        """Process the selected files."""
        # Validate inputs
        if not self.validate_inputs():
            return
        
        # Get input and output paths
        input_file = self.input_file_path.get()
        input_dir = self.input_dir_path.get()
        output_location = self.output_path.get()
        line_name = self.line_name.get()
        value = self.value.get()
        
        # Update status
        self.update_status("Processing started...")
        self.update_status(f"LineName/Option: {line_name}")
        self.update_status(f"Value: {value}")
        
        # Reset progress bar
        self.progress["value"] = 0
        self.root.update_idletasks()
        
        print('Processing files...')
        print('Input file:', input_file)

        # Simulate processing (replace with actual processing logic)
        self.simulate_processing(input_file, input_dir, output_location, line_name, value)
        
        # Complete the progress bar
        self.progress["value"] = 100
        self.root.update_idletasks()
        
        # Processing complete
        self.update_status(f"Processing complete! Output saved to {output_location}")
    
    def validate_inputs(self):
        """Validate user inputs before processing."""
        fields = [
            (self.input_file_path.get(), "Please select at input file"),
            (self.output_path.get(), "Please select an output location"),
            (self.line_name.get(), "Please enter a LineName/Option"),
            (self.value.get(), "Please enter a Value")
        ]
        
        for field, error_message in fields:
            if not field:
                self.status_text.config(state=tk.NORMAL)
                self.update_status(f"Error: {error_message}")
                self.status_text.config(state=tk.DISABLED)
                return False
        return True
    
    def simulate_processing(self, input_file, input_dir, output_location, line_name, value):
        """Simulate file processing (placeholder for actual processing)."""
        files_to_process = []

        if input_file:
            files_to_process.append(input_file)
            self.update_status(f"Processing file: {os.path.basename(input_file)}")

        if input_dir:
            try:
                # Get all files in the directory
                dir_files = [
                    os.path.join(input_dir, f) for f in os.listdir(input_dir)
                    if os.path.isfile(os.path.join(input_dir, f))
                ]
                files_to_process.extend(dir_files)
                self.update_status(f"Found {len(dir_files)} files in directory")
            except Exception as e:
                self.update_status(f"Error reading directory: {str(e)}")

        # Process each file (simulation)
        total_files = len(files_to_process)
        for i, file_path in enumerate(files_to_process):
            # Update progress
            progress_value = int((i / max(1, total_files)) * 100)
            self.progress["value"] = progress_value
            self.root.update_idletasks()

            # Simulate processing
            self.update_status(f"Processing {os.path.basename(file_path)}...")

            try:
                modified_file = self.processor.process_file(output_location, line_name, value, file_path)
                self.update_status(f"Processing complete! Saved as {modified_file}")
            except Exception as e:
                self.update_status(f"Error: {str(e)}")

            self.root.after(100)

