import tkinter as tk
from tkinter import PhotoImage

class RequestRobotPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.mainframe.columnconfigure(0, weight=1)
        self.current_page = 'Request Robot'

        # Navigation Bar-------------------------------------------------------------------------- 
        navbar_frame = tk.Frame(self.mainframe, height=150, background='#a0a9de')
        navbar_frame.pack(fill='x')

        buttons = ['Home', 'Request Robot', 'Feedback', 'Scan Area', 'Logout']
        self.nav_buttons = []
        for button_text in buttons:
            button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text, switch_frame), bg='#a0a9de', bd=0)
            button.config(height=4) 
            button.pack(side='left', fill='both', expand=True)
            self.nav_buttons.append(button)
            button.bind("<Enter>", self.on_button_hover)  # hover event

         # send_robot Page Content--------------------------------------------------------------------------
        left_frame = tk.Frame(self.mainframe, width=400, background='#333333')
        left_frame.pack(fill='y', side='left', pady=20, padx=30)
        
        right_frame = tk.Frame(self.mainframe, background='yellow', width=300)
        right_frame.pack(fill='y', side='right', pady=20, padx=30)

        selectDestinationLabel = tk.Label(left_frame, text="Select Destination")
        selectDestinationLabel.pack()

        options = ['Raum 1', 'Raum 2', 'Raum 3'] #todo: hier durch die Orte aus der Datenbank ergänzen.
        self.selected_option = tk.StringVar()
        orteDropdownMenu = tk.OptionMenu(left_frame, self.selected_option, *options)
        orteDropdownMenu.pack(padx=10, pady=5) 

        medicationLabel = tk.Label(left_frame, text="Enter Medication Name")
        medicationLabel.pack(padx=10, pady=5) 

        self.medication_entry = tk.Entry(left_frame)
        self.medication_entry.pack(padx=10, pady=5) 

        patientLabel = tk.Label(left_frame, text="Enter Patient Name")
        patientLabel.pack(padx=10, pady=5) 

        self.patient_entry = tk.Entry(left_frame)
        self.patient_entry.pack(padx=10, pady=5)

        confirmButton = tk.Button(left_frame, text="Confirm", command=lambda text=button_text: self.button_click(text, switch_frame))
        confirmButton.pack(side='left', fill='none', expand=True, padx=10, pady=5)

        #map
        image = PhotoImage(file="example_map.png")
        image_label = tk.Label(right_frame, image=image)
        image_label.pack(pady=20, anchor='center', expand=True)

    def button_click(self, button_text, switch_frame):
        if button_text == 'Logout':
            # Logout Firebase
            switch_frame('Login')
        elif button_text == 'Request Robot':
            switch_frame('Request Robot')
        elif button_text == 'Home':
            switch_frame('Home')
        elif button_text == "Confirm":
            pass
            

    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6' 

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de' 