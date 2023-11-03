import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')

        # Navigation Bar-------------------------------------------------------------------------- 
        navbar_frame = tk.Frame(self.mainframe, height=150, background='#a0a9de')
        navbar_frame.pack(fill='x')

        buttons = ['Home', 'Send Robot', 'Feedback', 'Scan Area', 'Logout']
        self.nav_buttons = []
        for button_text in buttons:
            button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text, switch_frame), bg='#a0a9de', bd=0)
            button.config(height=3) 
            button.pack(side='left', fill='both', expand=True)
            self.nav_buttons.append(button)
            button.bind("<Enter>", self.on_button_hover)  # hover event
            button.bind("<Leave>", self.on_button_leave)  # leave event

        # Home Page Content-------------------------------------------------------------------------- 
        left_frame = tk.Frame(self.mainframe, background='red', width=300)
        left_frame.pack(fill='y', side='left', pady=20, padx=30)
        
        right_frame = tk.Frame(self.mainframe, background='blue', width=400)
        right_frame.pack(fill='y', side='right', pady=20, padx=30)
        
        home_label = ttk.Label(left_frame, text='Medibot Home', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 45))
        home_label.pack(pady=20, fill='both', anchor='center',expand=True)

        status_label = ttk.Label(left_frame, text='current Status: connected', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 18))
        status_label.pack(pady=20)

    def button_click(self, button_text, switch_frame):
        if button_text == 'Logout':
            # Logout Firebase
            switch_frame('Login')
        elif button_text == 'Send Robot':
            switch_frame('Send Robot')
            pass    

    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6' 

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de'
