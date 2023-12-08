import tkinter as tk
from tkinter import ttk
from db import get_requests_with_status_delivering, get_current_user_email

class FeedbackPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.mainframe.columnconfigure(0, weight=1)
        self.current_page = 'Feedback'

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
        self.left_frame = tk.Frame(self.mainframe, width=350, height=400, background='#333333')
        self.right_frame = tk.Frame(self.mainframe)

        
        # fill labels
        requests_for_current_user = get_request_for_current_user() 
        
        if requests_for_current_user:
            self.left_frame.pack(fill='both', side='left', pady=60, padx=(60,0))
        else:
            empty_label = tk.Label(self.mainframe, text="None of your orders currently delivering.", background='#333333', foreground='white')
            empty_label.pack(pady=30)
            
        select_title_label = tk.Label(self.left_frame, text="Order Summary", background='#333333', foreground='white')
        select_title_label.config(font=("TkDefaultFont", 12, "bold"))
        select_title_label.grid(row=0,column=0,padx=10, pady=10, sticky='w')
        
        medication_label = tk.Label(self.left_frame, text="Medication", background='#333333', foreground='white')
        medication_label.grid(row=1,column=0,padx=10, pady=(5,0), sticky='w')
        
        quantity_label = tk.Label(self.left_frame, text="Quantity", background='#333333', foreground='white')
        quantity_label.grid(row=2,column=0,padx=10, pady=(5,0), sticky='w')
        
        location_label = tk.Label(self.left_frame, text="Location", background='#333333', foreground='white')
        location_label.grid(row=3,column=0,padx=10, pady=(5,0), sticky='w')
        
        patient_label = tk.Label(self.left_frame, text="Patient", background='#333333', foreground='white')
        patient_label.grid(row=4,column=0,padx=10, pady=(5,0), sticky='w')
        
        status_label = tk.Label(self.left_frame, text="Status: currently delivering..", background='#333333', foreground='white')
        status_label.grid(row=4,column=0,padx=10, pady=30, sticky='w')


       
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
    
    # show currently processed order
def get_request_for_current_user():
    current_user = get_current_user_email()
    user_requests_delivering = get_requests_with_status_delivering(current_user)
    return user_requests_delivering
            

    