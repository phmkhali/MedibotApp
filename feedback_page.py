import tkinter as tk
from tkinter import ttk

class FeedbackPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.mainframe.columnconfigure(0, weight=1)

        # Navigation Bar-------------------------------------------------------------------------- 
        navbar_frame = tk.Frame(self.mainframe, background='#a0a9de')
        navbar_frame.pack(fill='x')

        buttons = ['Home', 'Request Robot', 'Pending Requests', 'Feedback', 'Config']
        self.nav_buttons = []
        for button_text in buttons:
            button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text, switch_frame), bg='#a0a9de', bd=0)
            button.config(height=4) 
            button.pack(side='left', fill='both', expand=True)
            self.nav_buttons.append(button)
            button.bind("<Enter>", self.on_button_hover)  # hover event
            button.bind("<Leave>", self.on_button_leave)  # leave event
            
        # Update button colors
        for button in self.nav_buttons:
            if button.cget('text') == self.current_page:
                button['background'] = '#8c94c6'
            else:
                button['background'] = '#a0a9de'

        # Page Content-------------------------------------------------------------------------- 
        home_label = ttk.Label(self.mainframe, text='Feedback', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 14))
        home_label.pack(pady=20)

        placeholder_label = ttk.Label(self.mainframe, text='Welcome to Medibot. This is the home page.', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 12))
        placeholder_label.pack(pady=20)

    # Methods -------------------------------------------------------------------------- 
    def button_click(self, button_text, switch_frame):
            if button_text == 'Request Robot':
                switch_frame('Request Robot')
            elif button_text == 'Home':
                switch_frame('Home')
            elif button_text == 'Pending Requests':
                switch_frame('Pending Requests')     
            elif button_text == 'Feedback':
                switch_frame('Feedback')   
            elif button_text == "Confirm":
                pass
        
    def on_button_hover(self, event):
            event.widget['background'] = '#8c94c6' 

    def on_button_leave(self, event):
            event.widget['background'] = '#a0a9de' 
            

    