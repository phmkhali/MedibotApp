import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.mainframe.columnconfigure(0, weight=1)

        # Navigation Bar-------------------------------------------------------------------------- 
        navbar_frame = tk.Frame(self.mainframe, height=100, background='#a0a9de')
        navbar_frame.pack(fill='x')

        buttons = ['Home', 'Send Robot', 'Feedback', 'Scan Area', 'Logout']
        self.nav_buttons = []
        for button_text in buttons:
            button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text),bg='#a0a9de')
            button.pack(side='left', fill='both', expand=True)
            self.nav_buttons.append(button)

        # Home Page Content-------------------------------------------------------------------------- 
        home_label = ttk.Label(self.mainframe, text='Medibot Home', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 14))
        home_label.pack(pady=20)

        placeholder_label = ttk.Label(self.mainframe, text='Welcome to Medibot. This is the home page.', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 12))
        placeholder_label.pack(pady=20)

    def button_click(self, button_text):
        if button_text == 'Logout':
            # Implement the functionality to log out here
            pass
