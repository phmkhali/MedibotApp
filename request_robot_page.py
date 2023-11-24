import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from db import get_medication_db
from db import get_current_user_email
from db import create_request
from db import get_requests

class RequestRobotPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.current_page = 'Request Robot'


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
        left_frame = tk.Frame(self.mainframe, width=300, background='#333333')
        left_frame.pack(side='left', pady=20, padx=(60,30), anchor='center')

        right_frame = tk.Frame(self.mainframe, width=400)
        right_frame.pack(fill='both', side='right', pady=20, padx=30)

        select_destination_label = tk.Label(left_frame, text="Select Destination", background='#333333', foreground='white')
        select_destination_label.grid(row=0,column=0,padx=10, pady=5, sticky='w')

        options = ['Room 1', 'Room 2', 'Room 3'] #todo: hier durch die Orte aus der Datenbank ergänzen.
        self.selected_option = tk.StringVar()
        location_dropdown = ttk.OptionMenu(left_frame, self.selected_option, *options)
        location_dropdown.grid(row=1,column=0,padx=10, sticky='w')

        medication_label = tk.Label(left_frame, text="Enter Medication Name", background='#333333', foreground='white')
        medication_label.grid(row=2,column=0,padx=10, pady=10, sticky='w')

        # self updating combobox based on user input
        self.medication_var = tk.StringVar()
        self.medication_entry = ttk.Combobox(left_frame, width=24, textvariable=self.medication_var)
        self.medication_entry.grid(row=3,column=0,padx=10)
        self.medication_entry.bind("<KeyRelease>", self.update_combobox)

        quantity_label = tk.Label(left_frame, text="Enter Medication Quantity", background='#333333', foreground='white')
        quantity_label.grid(row=4,column=0,padx=10, pady=10, sticky='w')

        self.patient_entry = ttk.Entry(left_frame, width=24)
        self.patient_entry.grid(row=5,column=0,padx=10, sticky='w')

        patient_label = tk.Label(left_frame, text="Enter Patient Name", background='#333333', foreground='white')
        patient_label.grid(row=6,column=0,padx=10, pady=10, sticky='w')

        self.patient_entry = ttk.Entry(left_frame, width=24)
        self.patient_entry.grid(row=7,column=0,padx=10, sticky='w')

        confirm_button = tk.Button(left_frame, text="Confirm", background='#4C4273', relief='flat', foreground='white', command=self.show_messagebox, width=15)
        confirm_button.grid(row=8,column=0,padx=10, pady=20, sticky='w')

        #map
        image = PhotoImage(file="example_map.png")
        image_label = tk.Label(right_frame, image=image)
        image_label.pack(pady=20, anchor='center', expand=True)

    def button_click(self, button_text, switch_frame):
        if button_text == 'Request Robot':
            switch_frame('Request Robot')
        elif button_text == 'Home':
            switch_frame('Home')
        elif button_text == 'Pending Requests':
            switch_frame('Pending Requests')      
        elif button_text == "Confirm":
            pass
    
    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6' 

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de' 
        
    def show_messagebox(self):
        destination = self.selected_option.get()
        medication_name = self.medication_entry.get()
        medication_quantity = self.patient_entry.get()
        
        # Check if any entry fields are empty
        if not destination or not medication_name or not medication_quantity:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # who requested?
        current_user_name = get_current_user_email().split('@')[0]
        
        message = f"Destination: {destination}\nMedication Name: {medication_name}\nMedication Quantity: {medication_quantity}\nRequest from user: {current_user_name}"
        
        # create request in db
        create_request(destination,medication_name,medication_quantity)
        print(get_requests)
        
        messagebox.showinfo("Confirmation", message)

    def update_combobox(self):
        medication_names, _ = get_medication_db()  # Fetch medication names from the database
        user_input = self.medication_var.get().lower()

        if not user_input:
            # If nothing is written, show all medications
            self.medication_entry['values'] = medication_names
        else:
            # Filter medications based on user input
            matching_meds = [name for name in medication_names if user_input in name.lower()]
            self.medication_entry['values'] = matching_meds