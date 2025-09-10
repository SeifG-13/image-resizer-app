import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer Pro")
        self.root.geometry("520x650")
        self.root.resizable(False, False)
        
        # Modern color scheme
        self.colors = {
            'bg': '#1e1e1e',           # Dark background
            'surface': '#2d2d2d',       # Card background
            'primary': '#0078d4',       # Microsoft blue
            'primary_hover': '#106ebe', # Darker blue
            'secondary': '#00bcf2',     # Light blue
            'success': '#107c10',       # Green
            'warning': '#ff8c00',       # Orange
            'text': '#ffffff',          # White text
            'text_secondary': '#b3b3b3', # Light gray text
            'border': '#404040'         # Border color
        }
        
        # Configure root
        self.root.configure(bg=self.colors['bg'])
        
        # Variables
        self.input_path_var = tk.StringVar()
        self.output_path_var = tk.StringVar()
        self.width_var = tk.StringVar()
        self.height_var = tk.StringVar()
        
        # Create modern UI
        self.create_modern_ui()
        
    def create_modern_ui(self):
        """Create modern, sleek UI"""
        # Main container with padding
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill='both', expand=True, padx=25, pady=25)
        
        # Title section
        title_frame = tk.Frame(main_container, bg=self.colors['bg'])
        title_frame.pack(fill='x', pady=(0, 30))
        
        title_label = tk.Label(
            title_frame, 
            text="Image Resizer Pro",
            font=('Segoe UI', 24, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Resize images with professional quality",
            font=('Segoe UI', 11),
            fg=self.colors['text_secondary'],
            bg=self.colors['bg']
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Input file section
        self.create_section(main_container, "Select Image", self.create_input_section)
        
        # Presets section
        self.create_section(main_container, "Quick Presets", self.create_presets_section)
        
        # Custom dimensions section
        self.create_section(main_container, "Custom Dimensions", self.create_dimensions_section)
        
        # Output section
        self.create_section(main_container, "Output Location", self.create_output_section)
        
        # Action button
        self.create_action_button(main_container)
        
    def create_section(self, parent, title, content_func):
        """Create a modern section with title and content"""
        section_frame = tk.Frame(parent, bg=self.colors['bg'])
        section_frame.pack(fill='x', pady=(0, 25))
        
        # Section title
        title_label = tk.Label(
            section_frame,
            text=title,
            font=('Segoe UI', 14, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        title_label.pack(anchor='w', pady=(0, 10))
        
        # Content container with better styling
        content_frame = tk.Frame(
            section_frame,
            bg=self.colors['surface'],
            relief='solid',
            bd=1,
            highlightbackground=self.colors['border'],
            highlightthickness=1
        )
        content_frame.pack(fill='x', ipady=15, ipadx=15)
        
        # Create section content
        content_func(content_frame)
        
    def create_input_section(self, parent):
        """Create modern input file section"""
        input_container = tk.Frame(parent, bg=self.colors['surface'])
        input_container.pack(fill='x')
        
        # Entry with modern styling
        entry_frame = tk.Frame(input_container, bg=self.colors['surface'])
        entry_frame.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        self.input_entry = tk.Entry(
            entry_frame,
            textvariable=self.input_path_var,
            font=('Segoe UI', 10),
            bg=self.colors['bg'],
            fg=self.colors['text'],
            relief='solid',
            bd=1,
            insertbackground=self.colors['text']
        )
        self.input_entry.pack(fill='x', ipady=8, ipadx=10)
        
        # Modern browse button
        browse_btn = tk.Button(
            input_container,
            text="Browse",
            command=self.open_file,
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['primary'],
            fg=self.colors['text'],
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        browse_btn.pack(side='right')
        
        # Hover effects
        self.add_hover_effect(browse_btn, self.colors['primary'], self.colors['primary_hover'])
        
    def create_presets_section(self, parent):
        """Create presets section with only Hero and Product"""
        presets_container = tk.Frame(parent, bg=self.colors['surface'])
        presets_container.pack(fill='x')
        
        presets = [
            ("Hero (1259 × 1008)", 1259, 1008),
            ("Product (390 × 450)", 390, 450)
        ]
        
        for i, (name, w, h) in enumerate(presets):
            btn = tk.Button(
                presets_container,
                text=name,
                command=lambda w=w, h=h: self.set_dimensions(w, h),
                font=('Segoe UI', 11, 'bold'),
                bg=self.colors['secondary'],
                fg=self.colors['text'],
                relief='flat',
                bd=0,
                padx=30,
                pady=12,
                cursor='hand2'
            )
            
            if i == 0:
                btn.pack(side='left', padx=(0, 10), expand=True, fill='x')
            else:
                btn.pack(side='left', expand=True, fill='x')
                
            # Add hover effect
            self.add_hover_effect(btn, self.colors['secondary'], '#0099cc')
            
    def create_dimensions_section(self, parent):
        """Create modern dimensions input"""
        dims_container = tk.Frame(parent, bg=self.colors['surface'])
        dims_container.pack(fill='x')
        
        # Width input
        width_frame = tk.Frame(dims_container, bg=self.colors['surface'])
        width_frame.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        width_label = tk.Label(
            width_frame,
            text="Width (px)",
            font=('Segoe UI', 10, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['surface']
        )
        width_label.pack(anchor='w', pady=(0, 5))
        
        self.width_entry = tk.Entry(
            width_frame,
            textvariable=self.width_var,
            font=('Segoe UI', 11),
            bg=self.colors['bg'],
            fg=self.colors['text'],
            relief='solid',
            bd=1,
            justify='center',
            insertbackground=self.colors['text']
        )
        self.width_entry.pack(fill='x', ipady=10, ipadx=10)
        
        # Height input
        height_frame = tk.Frame(dims_container, bg=self.colors['surface'])
        height_frame.pack(side='left', fill='x', expand=True)
        
        height_label = tk.Label(
            height_frame,
            text="Height (px)",
            font=('Segoe UI', 10, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['surface']
        )
        height_label.pack(anchor='w', pady=(0, 5))
        
        self.height_entry = tk.Entry(
            height_frame,
            textvariable=self.height_var,
            font=('Segoe UI', 11),
            bg=self.colors['bg'],
            fg=self.colors['text'],
            relief='solid',
            bd=1,
            justify='center',
            insertbackground=self.colors['text']
        )
        self.height_entry.pack(fill='x', ipady=10, ipadx=10)
        
    def create_output_section(self, parent):
        """Create modern output section"""
        output_container = tk.Frame(parent, bg=self.colors['surface'])
        output_container.pack(fill='x')
        
        # Output entry
        entry_frame = tk.Frame(output_container, bg=self.colors['surface'])
        entry_frame.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        self.output_entry = tk.Entry(
            entry_frame,
            textvariable=self.output_path_var,
            font=('Segoe UI', 10),
            bg=self.colors['bg'],
            fg=self.colors['text'],
            relief='solid',
            bd=1,
            insertbackground=self.colors['text']
        )
        self.output_entry.pack(fill='x', ipady=8, ipadx=10)
        
        # Choose location button
        location_btn = tk.Button(
            output_container,
            text="Choose Location",
            command=self.choose_save_location,
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['warning'],
            fg=self.colors['text'],
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        location_btn.pack(side='right')
        
        # Hover effect
        self.add_hover_effect(location_btn, self.colors['warning'], '#e67c00')
        
    def create_action_button(self, parent):
        """Create the main action button"""
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill='x', pady=(20, 0))
        
        self.resize_button = tk.Button(
            button_frame,
            text="Resize Image",
            command=self.resize_action,
            font=('Segoe UI', 14, 'bold'),
            bg=self.colors['success'],
            fg=self.colors['text'],
            relief='flat',
            bd=0,
            padx=40,
            pady=15,
            cursor='hand2',
            state='disabled'
        )
        self.resize_button.pack(anchor='center')
        
        # Hover effect for enabled state
        self.add_hover_effect(self.resize_button, self.colors['success'], '#0e6b0e')
        
        # Bind input changes to enable/disable button
        self.input_path_var.trace('w', self.validate_inputs)
        self.output_path_var.trace('w', self.validate_inputs)
        self.width_var.trace('w', self.validate_inputs)
        self.height_var.trace('w', self.validate_inputs)
        
    def add_hover_effect(self, widget, normal_color, hover_color):
        """Add hover effect to buttons"""
        def on_enter(e):
            if widget['state'] != 'disabled':
                widget.config(bg=hover_color)
        
        def on_leave(e):
            if widget['state'] != 'disabled':
                widget.config(bg=normal_color)
                
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
        
    def validate_inputs(self, *args):
        """Enable/disable resize button based on inputs"""
        if (self.input_path_var.get().strip() and 
            self.output_path_var.get().strip() and 
            self.width_var.get().strip() and 
            self.height_var.get().strip()):
            self.resize_button.config(
                state='normal',
                bg=self.colors['success']
            )
        else:
            self.resize_button.config(
                state='disabled',
                bg='#666666'
            )
            
    def set_dimensions(self, width, height):
        """Set predefined dimensions"""
        self.width_var.set(str(width))
        self.height_var.set(str(height))
        
    def open_file(self):
        """Open file dialog to select image"""
        file_path = filedialog.askopenfilename(
            title="Select an image to resize",
            filetypes=[
                ("All Images", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.webp"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("PNG files", "*.png"),
                ("BMP files", "*.bmp"),
                ("GIF files", "*.gif"),
                ("TIFF files", "*.tiff"),
                ("WebP files", "*.webp"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            self.input_path_var.set(file_path)
            
            # Auto-suggest output location with better path handling
            if not self.output_path_var.get().strip():
                directory = os.path.dirname(file_path)
                name, ext = os.path.splitext(os.path.basename(file_path))
                suggested_output = os.path.join(directory, f"{name}_resized{ext}")
                self.output_path_var.set(suggested_output)
                
    def choose_save_location(self):
        """Choose where to save the resized image"""
        # Get initial values
        input_path = self.input_path_var.get().strip()
        current_output = self.output_path_var.get().strip()
        
        # Determine initial directory and filename
        if input_path and os.path.exists(input_path):
            initial_dir = os.path.dirname(input_path)
            name, ext = os.path.splitext(os.path.basename(input_path))
            default_filename = f"{name}_resized{ext}"
        elif current_output:
            initial_dir = os.path.dirname(current_output) if os.path.dirname(current_output) else os.getcwd()
            default_filename = os.path.basename(current_output)
            ext = os.path.splitext(default_filename)[1] if os.path.splitext(default_filename)[1] else '.jpg'
        else:
            initial_dir = os.getcwd()
            default_filename = "resized_image.jpg"
            ext = '.jpg'
        
        # Ensure initial directory exists
        if not os.path.exists(initial_dir):
            initial_dir = os.getcwd()
        
        file_path = filedialog.asksaveasfilename(
            title="Choose where to save the resized image",
            initialdir=initial_dir,
            initialfile=default_filename,
            defaultextension=ext,
            filetypes=[
                ("JPEG files", "*.jpg"),
                ("PNG files", "*.png"),
                ("BMP files", "*.bmp"),
                ("GIF files", "*.gif"),
                ("TIFF files", "*.tiff"),
                ("WebP files", "*.webp"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.output_path_var.set(file_path)
            
    def resize_image(self, input_path, output_path, width, height):
        """Resize image with high quality"""
        try:
            # Validate input file exists
            if not os.path.exists(input_path):
                messagebox.showerror("Error", f"Input file does not exist:\n{input_path}")
                return False
            
            # Ensure output directory exists
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                try:
                    os.makedirs(output_dir, exist_ok=True)
                except OSError as e:
                    messagebox.showerror("Error", f"Cannot create output directory:\n{output_dir}\n\nError: {str(e)}")
                    return False
            
            # Open and resize image
            with Image.open(input_path) as img:
                # Use high-quality resampling
                img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
                
                # Save with appropriate quality settings
                save_kwargs = {'optimize': True}
                if output_path.lower().endswith(('.jpg', '.jpeg')):
                    save_kwargs['quality'] = 95
                elif output_path.lower().endswith('.png'):
                    save_kwargs['compress_level'] = 6
                
                img_resized.save(output_path, **save_kwargs)
                return True
                
        except PermissionError as e:
            messagebox.showerror("Permission Error", 
                f"Cannot write to the selected location:\n{output_path}\n\n"
                f"Error: {str(e)}\n\nPlease choose a different location or run as administrator.")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Error resizing image:\n{str(e)}")
            return False
            
    def resize_action(self):
        """Handle resize button click"""
        input_path = self.input_path_var.get().strip()
        output_path = self.output_path_var.get().strip()
        
        # Validation
        if not input_path:
            messagebox.showerror("Error", "Please select an input image.")
            return
            
        if not os.path.exists(input_path):
            messagebox.showerror("Error", "The selected input file does not exist.")
            return
            
        if not output_path:
            messagebox.showerror("Error", "Please choose an output location.")
            return
            
        # Check if input and output are the same file
        try:
            if os.path.abspath(input_path) == os.path.abspath(output_path):
                result = messagebox.askyesno("Overwrite Warning", 
                    "The output path is the same as the input file.\n\n"
                    "This will overwrite the original image. Continue?")
                if not result:
                    return
        except:
            pass  # If path comparison fails, continue anyway
            
        # Validate dimensions
        try:
            width = int(self.width_var.get().strip())
            height = int(self.height_var.get().strip())
            
            if width <= 0 or height <= 0:
                raise ValueError("Dimensions must be positive numbers.")
                
            if width > 20000 or height > 20000:
                result = messagebox.askyesno("Warning", 
                    f"Very large dimensions detected ({width} × {height}).\n"
                    f"This may take a while and use lots of memory. Continue?")
                if not result:
                    return
                
        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid dimensions (positive integers).")
            return
            
        # Disable button during processing
        original_text = self.resize_button.cget('text')
        self.resize_button.config(
            state='disabled', 
            text="Processing...",
            bg='#666666'
        )
        self.root.update()
        
        try:
            # Perform resize
            success = self.resize_image(input_path, output_path, width, height)
            
            if success:
                # Show success message
                result = messagebox.askyesno("Success", 
                    f"✅ Image resized successfully!\n\n"
                    f"Original: {os.path.basename(input_path)}\n"
                    f"Resized: {os.path.basename(output_path)}\n"
                    f"New Size: {width} × {height} pixels\n\n"
                    f"Open the folder containing the resized image?")
                
                if result:
                    # Open folder containing the file
                    folder_path = os.path.dirname(output_path)
                    self.open_folder(folder_path)
                            
        finally:
            # Re-enable button
            self.resize_button.config(
                state='normal', 
                text=original_text,
                bg=self.colors['success']
            )
    
    def open_folder(self, folder_path):
        """Open folder in file explorer (cross-platform)"""
        import subprocess
        import platform
        
        try:
            if platform.system() == "Windows":
                os.startfile(folder_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", folder_path])
            else:  # Linux and others
                subprocess.run(["xdg-open", folder_path])
        except Exception as e:
            messagebox.showinfo("Info", 
                f"Resized image saved to:\n{folder_path}\n\n"
                f"Could not open folder automatically: {str(e)}")

def main():
    root = tk.Tk()
    
    # Set window icon (optional)
    try:
        root.iconbitmap("icon.ico")
    except:
        pass
    
    app = ImageResizerApp(root)
    
    # Center the window
    root.update_idletasks()
    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    # Prevent window from appearing behind other windows
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    
    root.mainloop()

if __name__ == "__main__":
    main()