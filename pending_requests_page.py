import tkinter as tk
from tkinter import ttk

class PendingRequestsPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.current_page = 'Pending Requests'


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
        self.placeholder_frame = tk.Frame(self.mainframe, width=250, background='#333333')
        self.placeholder_frame.pack(side='right', padx=30, pady= 20, fill='y')

        self.left_frame = tk.Frame(self.mainframe, background='green')
        self.left_frame.pack(fill='both', side='left', pady=20, padx=30, expand=True)
        
        self.right_frame = tk.Frame(self.placeholder_frame)
        self.right_frame.pack_forget()
        
        # todo: Liste sinnvoll befüllen
        requestList = (("Paracetamol 500 ", 2,"Room 3"),("Ibuprofen 800", 3, "Room 2"),("Calcium Sandoz 500",1,"Room 2"))
        
        # tree
        tree = ttk.Treeview(self.left_frame, columns=("Medication", "Quantity", "Room"), show="headings")
        tree.heading("Medication", text="Medication")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Room", text="Room")
        
        tree.column("Medication", width=150)  # Adjust the width as needed
        tree.column("Quantity", width=50)     # Adjust the width as needed
        tree.column("Room", width=50)         # Adjust the width as needed

        # Add data to the treeview
        for item in requestList:
            tree.insert("", tk.END, values=item)

        tree.pack(expand=True, fill='both')
        tree.bind("<<TreeviewSelect>>", self.on_select)

        self.med_qty_label = ttk.Label(self.right_frame, text="")
        self.med_qty_label.pack()
        
        self.location_label = ttk.Label(self.right_frame, text="")
        self.location_label.pack()
        
        self.request_from_label = ttk.Label(self.right_frame, text="")
        self.request_from_label.pack()

        self.right_frame.rowconfigure(1, weight=1)
        
        # submit button
        submit_button = tk.Button(self.right_frame,  relief='flat', background='#4C4273', foreground='white', width='12', text="Submit", command=lambda text=button_text: self.button_click(text, switch_frame) )
        submit_button.pack(side='bottom',pady=10)  

    def on_select(self, event):
        self.med_qty_label["text"] = ""
        self.location_label["text"] = ""
        self.request_from_label["text"] = ""
        selection = event.widget.selection()

        if selection:
            selected_item = event.widget.item(selection, 'values')
            
            self.med_qty_label["text"] = f"Selected Item: {selected_item[1]}x {selected_item[0]}"
            self.location_label["text"] = f"Send to: {selected_item[2]}"
            self.request_from_label["text"] = "Doctor Smith"
            
            self.right_frame.pack(side='right', padx=30, pady= 20, fill='both',expand=True)
        else:
            self.right_frame.pack_forget()

    def button_click(self, button_text, switch_frame):
        if button_text == 'Logout':
            # Logout Firebase
            switch_frame('Login')
        elif button_text == 'Request Robot':
            switch_frame('Request Robot')
        elif button_text == 'Home':
            switch_frame('Home')
        elif button_text == "Submit":
            pass #hier dann die progess bar!
    
    
    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6' 

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de' 