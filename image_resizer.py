import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer Pro")
        self.root.geometry("700x750")
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
        self.selected_images = []  # Store list of selected image paths
        self.selected_image_widgets = []  # Store widgets that are currently selected for removal
        self.image_preview_widgets = []  # Store all image preview widgets
        
        # Create modern UI
        self.create_modern_ui()
        
    def create_modern_ui(self):
        """Create modern, sleek UI"""
        # Main container with padding
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill='both', expand=True, padx=15, pady=10)
        
        # Title section
        title_frame = tk.Frame(main_container, bg=self.colors['bg'])
        title_frame.pack(fill='x', pady=(0, 15))
        
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
        subtitle_label.pack(pady=(2, 0))
        
        # Input file section
        self.create_section(main_container, "Select Images", self.create_input_section)
        
        # Presets section
        self.create_section(main_container, "Quick Presets", self.create_presets_section)
        
        # Custom dimensions section
        self.create_section(main_container, "Custom Dimensions", self.create_dimensions_section)
        
        # Output section
        self.create_section(main_container, "Output Location", self.create_output_section)
        
        # Progress section (initially hidden)
        self.create_progress_section(main_container)
        
        # Action button
        self.create_action_button(main_container)
        
    def create_section(self, parent, title, content_func):
        """Create a modern section with title and content"""
        section_frame = tk.Frame(parent, bg=self.colors['bg'])
        section_frame.pack(fill='x', pady=(0, 15))
        
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
        content_frame.pack(fill='x', ipady=10, ipadx=15)
        
        # Create section content
        content_func(content_frame)
        
    def create_input_section(self, parent):
        """Create modern input file section with multiple image support"""
        input_container = tk.Frame(parent, bg=self.colors['surface'])
        input_container.pack(fill='x')
        
        # Button controls
        button_frame = tk.Frame(input_container, bg=self.colors['surface'])
        button_frame.pack(fill='x', pady=(0, 10))
        
        # Browse multiple images button
        browse_btn = tk.Button(
            button_frame,
            text="Select Images",
            command=self.open_multiple_files,
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['primary'],
            fg=self.colors['text'],
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        browse_btn.pack(side='left', padx=(0, 10))
        
        # Clear selection button
        clear_btn = tk.Button(
            button_frame,
            text="Clear All",
            command=self.clear_selection,
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['warning'],
            fg=self.colors['text'],
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        clear_btn.pack(side='left', padx=(0, 10))
        
        # Remove selected button
        remove_btn = tk.Button(
            button_frame,
            text="Remove Selected",
            command=self.remove_selected_image,
            font=('Segoe UI', 10, 'bold'),
            bg='#d13438',  # Red color
            fg=self.colors['text'],
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        remove_btn.pack(side='left')
        
        # Selected images display
        self.images_display_frame = tk.Frame(input_container, bg=self.colors['surface'])
        self.images_display_frame.pack(fill='x')
        
        # Status label for selected images
        self.selected_count_label = tk.Label(
            self.images_display_frame,
            text="No images selected",
            font=('Segoe UI', 10),
            fg=self.colors['text_secondary'],
            bg=self.colors['surface']
        )
        self.selected_count_label.pack(anchor='w', pady=(5, 10))
        
        # Scrollable frame for image grid
        self.create_scrollable_image_grid()
        
        # Hover effects
        self.add_hover_effect(browse_btn, self.colors['primary'], self.colors['primary_hover'])
        self.add_hover_effect(clear_btn, self.colors['warning'], '#e67c00')
        self.add_hover_effect(remove_btn, '#d13438', '#b12328')
    
    def create_scrollable_image_grid(self):
        """Create scrollable grid for image previews"""
        # Main container for scrollable content
        canvas_container = tk.Frame(self.images_display_frame, bg=self.colors['surface'])
        canvas_container.pack(fill='both', expand=True)
        
        # Canvas for scrolling
        self.image_canvas = tk.Canvas(
            canvas_container,
            bg=self.colors['surface'],
            height=120,  # Fixed height for preview area
            highlightthickness=0
        )
        
        # Scrollbar for canvas
        scrollbar_v = tk.Scrollbar(canvas_container, orient='vertical', command=self.image_canvas.yview)
        self.image_canvas.configure(yscrollcommand=scrollbar_v.set)
        
        # Scrollable frame inside canvas
        self.scrollable_frame = tk.Frame(self.image_canvas, bg=self.colors['surface'])
        self.canvas_window = self.image_canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        
        # Pack canvas and scrollbar
        self.image_canvas.pack(side='left', fill='both', expand=True)
        scrollbar_v.pack(side='right', fill='y')
        
        # Bind mousewheel to canvas
        self.image_canvas.bind('<Configure>', self._on_canvas_configure)
        self.scrollable_frame.bind('<Configure>', self._on_frame_configure)
        
        # Bind mousewheel events
        self._bind_mousewheel()
    
    def _on_canvas_configure(self, event):
        """Handle canvas resize"""
        self.image_canvas.itemconfig(self.canvas_window, width=event.width)
    
    def _on_frame_configure(self, event):
        """Handle frame resize"""
        self.image_canvas.configure(scrollregion=self.image_canvas.bbox('all'))
    
    def _bind_mousewheel(self):
        """Bind mousewheel events for scrolling"""
        def _on_mousewheel(event):
            self.image_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def _bind_to_mousewheel(event):
            self.image_canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def _unbind_from_mousewheel(event):
            self.image_canvas.unbind_all("<MouseWheel>")
        
        self.image_canvas.bind('<Enter>', _bind_to_mousewheel)
        self.image_canvas.bind('<Leave>', _unbind_from_mousewheel)
    
    def create_image_thumbnail(self, image_path, size=(120, 120)):
        """Create thumbnail from image path"""
        try:
            with Image.open(image_path) as img:
                # Convert to RGB if necessary (for PNG with transparency, etc.)
                if img.mode in ('RGBA', 'LA'):
                    # Create a white background
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'RGBA':
                        background.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
                    else:
                        background.paste(img)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Create thumbnail maintaining aspect ratio
                img.thumbnail(size, Image.Resampling.LANCZOS)
                
                # Create a new image with fixed size and center the thumbnail
                thumb = Image.new('RGB', size, (45, 45, 45))  # Dark background
                x = (size[0] - img.width) // 2
                y = (size[1] - img.height) // 2
                thumb.paste(img, (x, y))
                
                return thumb
        except Exception as e:
            # Return a placeholder image if thumbnail creation fails
            placeholder = Image.new('RGB', size, (100, 100, 100))
            return placeholder
    
    def create_image_preview_widget(self, image_path, index):
        """Create a preview widget for an image"""
        # Create container frame
        preview_frame = tk.Frame(
            self.scrollable_frame,
            bg=self.colors['bg'],
            relief='solid',
            bd=2,
            cursor='hand2',
            padx=5,
            pady=5
        )
        
        # Create thumbnail
        thumbnail = self.create_image_thumbnail(image_path)
        
        # Convert PIL image to PhotoImage
        import io
        import base64
        
        # Save thumbnail to bytes and convert to base64
        img_bytes = io.BytesIO()
        thumbnail.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        img_data = base64.b64encode(img_bytes.read())
        
        # Create PhotoImage from base64 data
        photo = tk.PhotoImage(data=img_data)
        
        # Image label
        img_label = tk.Label(
            preview_frame,
            image=photo,
            bg=self.colors['bg'],
            cursor='hand2'
        )
        img_label.image = photo  # Keep reference
        img_label.pack(pady=5)
        
        # Filename label
        filename = os.path.basename(image_path)
        if len(filename) > 15:
            display_name = filename[:12] + "..."
        else:
            display_name = filename
            
        name_label = tk.Label(
            preview_frame,
            text=display_name,
            font=('Segoe UI', 8),
            fg=self.colors['text'],
            bg=self.colors['bg'],
            cursor='hand2'
        )
        name_label.pack(pady=(0, 5))
        
        # Store references
        preview_frame.image_path = image_path
        preview_frame.index = index
        preview_frame.selected = False
        
        # Bind click events
        def on_click(event):
            self.toggle_image_selection(preview_frame)
        
        preview_frame.bind('<Button-1>', on_click)
        img_label.bind('<Button-1>', on_click)
        name_label.bind('<Button-1>', on_click)
        
        return preview_frame
    
    def toggle_image_selection(self, widget):
        """Toggle selection state of an image widget"""
        if widget.selected:
            # Deselect
            widget.selected = False
            widget.config(
                bg=self.colors['bg'], 
                highlightbackground=self.colors['bg'],
                relief='solid',
                bd=2
            )
            # Update all child widgets
            for child in widget.winfo_children():
                child.config(bg=self.colors['bg'])
            if widget in self.selected_image_widgets:
                self.selected_image_widgets.remove(widget)
        else:
            # Select
            widget.selected = True
            widget.config(
                bg=self.colors['primary'], 
                highlightbackground=self.colors['primary'],
                relief='solid',
                bd=3
            )
            # Update all child widgets
            for child in widget.winfo_children():
                child.config(bg=self.colors['primary'])
            self.selected_image_widgets.append(widget)
        
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
    
    def create_progress_section(self, parent):
        """Create progress section for batch processing"""
        self.progress_section_frame = tk.Frame(parent, bg=self.colors['bg'])
        self.progress_section_frame.pack(fill='x', pady=(0, 15))
        self.progress_section_frame.pack_forget()  # Hide initially
        
        # Section title
        progress_title = tk.Label(
            self.progress_section_frame,
            text="Processing Progress",
            font=('Segoe UI', 14, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        progress_title.pack(anchor='w', pady=(0, 10))
        
        # Progress container
        progress_container = tk.Frame(
            self.progress_section_frame,
            bg=self.colors['surface'],
            relief='solid',
            bd=1,
            highlightbackground=self.colors['border'],
            highlightthickness=1
        )
        progress_container.pack(fill='x', ipady=8, ipadx=15)
        
        # Progress label
        self.progress_label = tk.Label(
            progress_container,
            text="Ready to process",
            font=('Segoe UI', 11),
            fg=self.colors['text'],
            bg=self.colors['surface']
        )
        self.progress_label.pack(anchor='w', pady=(0, 10))
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            progress_container,
            variable=self.progress_var,
            mode='determinate',
            length=400
        )
        self.progress_bar.pack(fill='x', pady=(0, 5))
        
        # Progress percentage
        self.progress_percent_label = tk.Label(
            progress_container,
            text="0%",
            font=('Segoe UI', 10),
            fg=self.colors['text_secondary'],
            bg=self.colors['surface']
        )
        self.progress_percent_label.pack(anchor='w')
        
    def create_action_button(self, parent):
        """Create the main action button"""
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill='x', pady=(10, 0))
        
        self.resize_button = tk.Button(
            button_frame,
            text="Resize Images",
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
        if (len(self.selected_images) > 0 and 
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
        
    def open_multiple_files(self):
        """Open file dialog to select multiple images"""
        file_paths = filedialog.askopenfilenames(
            title="Select images to resize",
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
        if file_paths:
            # Add new files to existing selection (avoid duplicates)
            for file_path in file_paths:
                if file_path not in self.selected_images:
                    self.selected_images.append(file_path)
            
            self.update_images_display()
            
            # Auto-suggest output location if not set
            if not self.output_path_var.get().strip() and self.selected_images:
                directory = os.path.dirname(self.selected_images[0])
                self.output_path_var.set(directory)
    
    def clear_selection(self):
        """Clear all selected images"""
        self.selected_images = []
        self.update_images_display()
    
    def remove_selected_image(self):
        """Remove currently selected images from grid"""
        if self.selected_image_widgets:
            # Get indices of selected widgets and sort in reverse order
            indices_to_remove = []
            for widget in self.selected_image_widgets:
                if hasattr(widget, 'index') and widget.index < len(self.selected_images):
                    indices_to_remove.append(widget.index)
            
            # Sort in reverse order to avoid index shifting issues
            indices_to_remove.sort(reverse=True)
            
            # Remove images
            for index in indices_to_remove:
                if 0 <= index < len(self.selected_images):
                    self.selected_images.pop(index)
            
            self.update_images_display()
        else:
            messagebox.showinfo("No Selection", "Please click on images to select them for removal.")
    
    def update_images_display(self):
        """Update the display of selected images with grid layout"""
        # Clear existing widgets
        for widget in self.image_preview_widgets:
            widget.destroy()
        self.image_preview_widgets.clear()
        self.selected_image_widgets.clear()
        
        # Update count label
        count = len(self.selected_images)
        if count == 0:
            self.selected_count_label.config(text="No images selected")
        elif count == 1:
            self.selected_count_label.config(text="1 image selected")
        else:
            self.selected_count_label.config(text=f"{count} images selected")
        
        # Create grid of image previews
        if self.selected_images:
            cols = 3  # Number of columns in grid
            for i, img_path in enumerate(self.selected_images):
                row = i // cols
                col = i % cols
                
                # Create preview widget
                preview_widget = self.create_image_preview_widget(img_path, i)
                preview_widget.grid(row=row, column=col, padx=5, pady=5, sticky='n')
                
                self.image_preview_widgets.append(preview_widget)
        
        # Update scroll region
        self.scrollable_frame.update_idletasks()
        self.image_canvas.configure(scrollregion=self.image_canvas.bbox('all'))
        
        # Validate inputs after updating selection
        self.validate_inputs()
                
    def choose_save_location(self):
        """Choose where to save the resized images"""
        # For multiple images, choose a folder
        if len(self.selected_images) > 1:
            folder_path = filedialog.askdirectory(
                title="Choose folder to save resized images",
                initialdir=os.path.dirname(self.selected_images[0]) if self.selected_images else os.getcwd()
            )
            if folder_path:
                self.output_path_var.set(folder_path)
        
        # For single image, choose specific file
        elif len(self.selected_images) == 1:
            input_path = self.selected_images[0]
            initial_dir = os.path.dirname(input_path)
            name, ext = os.path.splitext(os.path.basename(input_path))
            default_filename = f"{name}_resized{ext}"
            
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
        
        # No images selected
        else:
            folder_path = filedialog.askdirectory(
                title="Choose output folder",
                initialdir=os.getcwd()
            )
            if folder_path:
                self.output_path_var.set(folder_path)
            
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
        """Handle resize button click for batch processing"""
        # Validation
        if not self.selected_images:
            messagebox.showerror("Error", "Please select images to resize.")
            return
            
        output_path = self.output_path_var.get().strip()
        if not output_path:
            messagebox.showerror("Error", "Please choose an output location.")
            return
            
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
        
        # Start batch processing
        self.process_batch_resize(width, height, output_path)
    
    def process_batch_resize(self, width, height, output_location):
        """Process multiple images with progress tracking"""
        total_images = len(self.selected_images)
        successful_resizes = 0
        failed_resizes = []
        
        # Show progress section
        self.progress_section_frame.pack(fill='x', pady=(0, 15))
        
        # Disable button during processing
        original_text = self.resize_button.cget('text')
        self.resize_button.config(
            state='disabled', 
            text="Processing...",
            bg='#666666'
        )
        
        # Initialize progress
        self.progress_var.set(0)
        self.progress_percent_label.config(text="0%")
        self.progress_label.config(text="Starting batch resize...")
        self.root.update()
        
        try:
            for i, input_path in enumerate(self.selected_images):
                # Update progress
                progress_percent = int((i / total_images) * 100)
                self.progress_var.set(progress_percent)
                self.progress_percent_label.config(text=f"{progress_percent}%")
                
                filename = os.path.basename(input_path)
                self.progress_label.config(text=f"Processing: {filename} ({i+1}/{total_images})")
                self.root.update()
                
                # Determine output path for this image
                if total_images == 1 and not os.path.isdir(output_location):
                    # Single image, specific file path
                    current_output_path = output_location
                else:
                    # Multiple images or folder selected, create filename
                    name, ext = os.path.splitext(os.path.basename(input_path))
                    output_filename = f"{name}_resized{ext}"
                    current_output_path = os.path.join(output_location, output_filename)
                
                # Resize image
                success = self.resize_image(input_path, current_output_path, width, height)
                
                if success:
                    successful_resizes += 1
                else:
                    failed_resizes.append(filename)
            
            # Final progress update
            self.progress_var.set(100)
            self.progress_percent_label.config(text="100%")
            self.progress_label.config(text="Batch resize completed!")
            self.root.update()
            
            # Show completion message
            if failed_resizes:
                message = f"✅ Batch resize completed!\n\n"
                message += f"Successfully resized: {successful_resizes}/{total_images} images\n"
                message += f"Failed: {len(failed_resizes)} images\n"
                message += f"New Size: {width} × {height} pixels\n\n"
                message += f"Failed files:\n" + "\n".join(failed_resizes[:5])
                if len(failed_resizes) > 5:
                    message += f"\n... and {len(failed_resizes) - 5} more"
                message += f"\n\nOpen the output folder?"
                
                result = messagebox.askyesno("Batch Resize Completed", message)
            else:
                result = messagebox.askyesno("Success", 
                    f"✅ All images resized successfully!\n\n"
                    f"Processed: {successful_resizes} images\n"
                    f"New Size: {width} × {height} pixels\n\n"
                    f"Open the output folder?")
            
            if result:
                # Open output folder
                if total_images == 1 and not os.path.isdir(output_location):
                    folder_path = os.path.dirname(output_location)
                else:
                    folder_path = output_location
                self.open_folder(folder_path)
            
            # Clear selection automatically after successful batch resize
            if successful_resizes > 0:
                self.clear_selection()
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during batch processing:\n{str(e)}")
        
        finally:
            # Re-enable button and hide progress
            self.resize_button.config(
                state='normal', 
                text=original_text,
                bg=self.colors['success']
            )
            # Keep progress visible for a moment, then hide
            self.root.after(3000, self.progress_section_frame.pack_forget)
    
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