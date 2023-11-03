import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

class HomePage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')

        # Navigation Bar-------------------------------------------------------------------------- 
        navbar_frame = tk.Frame(self.mainframe, background='#a0a9de')
        navbar_frame.pack(fill='x')

        buttons = ['Home', 'Send Robot', 'Feedback', 'Scan Area', 'Logout']
        self.nav_buttons = []
        for button_text in buttons:
            button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text, switch_frame), bg='#a0a9de', bd=0)
            button.config(height=4) 
            button.pack(side='left', fill='both', expand=True)
            self.nav_buttons.append(button)
            button.bind("<Enter>", self.on_button_hover)  # hover event
            button.bind("<Leave>", self.on_button_leave)  # leave event

        # Home Page Content-------------------------------------------------------------------------- 
        left_frame = tk.Frame(self.mainframe, width=300, background='#333333')
        left_frame.pack(fill='y', side='left', pady=20, padx=(40,0))
        
        right_frame = tk.Frame(self.mainframe, background='#333333', width=400)
        right_frame.pack(fill='y', side='right', pady=20, padx=40)
        
        home_label = ttk.Label(left_frame, text='Medibot', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 45))
        home_label.pack(pady=20, anchor='center', expand=True)

        # map
        image = PhotoImage(file="example_map.png")
        image_label = tk.Label(right_frame, image=image)
        image_label.pack(pady=20, anchor='center', expand=True)

        # Status
        self.status_indicator = ttk.Label(left_frame, text='', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 18))
        self.status_indicator.pack(pady=20)
        
        self.status_canvas = tk.Canvas(left_frame, width=20, height=20, background='#333333', bd=0, highlightthickness=0)
        self.status_canvas.pack(pady=20)
        self.status_canvas.create_oval(2, 2, 18, 18, fill='green', outline='#333333', tags="status_indicator") 
        self.update_status('connected')  # Initial status

    def update_status(self, status):
        if status == 'connected':
                self.status_indicator.config(text='Status: connected')
                self.status_canvas.itemconfig("status_indicator", fill='green')  
        else:
                self.status_indicator.config(text='Status: disconnected')
                self.status_canvas.itemconfig("status_indicator", fill='red') 

    def button_click(self, button_text, switch_frame):
        if button_text == 'Logout':
            # Logout Firebase
            switch_frame('Login')
        elif button_text == 'Send Robot':
            switch_frame('Send Robot')

    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6'

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de'
