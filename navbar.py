import tkinter as tk
from tkinter import ttk
from db import sign_out

# reusable navbar for all tabs
def create_navbar(mainframe, switch_frame):
    navbar_frame = tk.Frame(mainframe, background='#a0a9de')
    navbar_frame.pack(fill='x')

    # tab names
    buttons = ['Home', 'Request Robot', 'Pending Requests', 'Feedback']
    nav_buttons = []

    # make button darker on hover
    def on_button_hover(event):
        event.widget['background'] = '#8c94c6' 
    def on_button_leave(event):
        event.widget['background'] = '#a0a9de' 

    for button_text in buttons:
        # customize buttons
        button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: button_click(text), bg='#a0a9de', bd=0)
        button.config(height=4) 
        button.pack(side='left', fill='both', expand=True)
        nav_buttons.append(button)
        button.bind("<Enter>", on_button_hover)  
        button.bind("<Leave>", on_button_leave) 

    def button_click(text): 
        for button in nav_buttons:
            button['background'] = '#a0a9de'
        if text == 'Home':
            switch_frame('Home')
        elif text == 'Log out':
            sign_out()  
        elif text == 'Request Robot':
            switch_frame('Request Robot')
        elif text == 'Pending Requests':
            switch_frame('Pending Requests')  
        elif text == 'Feedback':
            switch_frame('Feedback')  
        else:
            switch_frame(text)
