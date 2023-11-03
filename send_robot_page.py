import tkinter as tk

class SendRobotPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.mainframe.columnconfigure(0, weight=1)

        # Navigation Bar-------------------------------------------------------------------------- 
        navbar_frame = tk.Frame(self.mainframe, height=150, background='#a0a9de')
        navbar_frame.pack(fill='x')

        buttons = ['Home', 'Send Robot', 'Feedback', 'Scan Area', 'Logout']
        self.nav_buttons = []
        for button_text in buttons:
            button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text), bg='#a0a9de', bd=0)
            button.config(height=3) 
            button.pack(side='left', fill='both', expand=True)
            self.nav_buttons.append(button)
            button.bind("<Enter>", self.on_button_hover)  # hover event

         # send_robot Page Content--------------------------------------------------------------------------
        selectDestinationLabel = tk.Label(self.mainframe, text="Select Destination")
        selectDestinationLabel.pack()

        options = ['Raum 1', 'Raum 2', 'Raum 3'] #todo: hier durch die Orte aus der Datenbank ergänzen.
        self.selected_option = tk.StringVar()
        orteDropdownMenu = tk.OptionMenu(self.mainframe, self.selected_option, *options)
        orteDropdownMenu.pack()

        medicationLabel = tk.Label(self.mainframe, text="Enter Medication Name")
        medicationLabel.pack()

        self.medication_entry = tk.Entry(self.mainframe)
        self.medication_entry.pack()

        patientLabel = tk.Label(self.mainframe, text="Enter Patient Name")
        patientLabel.pack()

        self.patient_entry = tk.Entry(self.mainframe)
        self.patient_entry.pack()
        
    def button_click(self, button_text, switch_frame):
        if button_text == 'Logout':
            # Logout Firebase
            switch_frame('Login')

    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6' 

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de' 