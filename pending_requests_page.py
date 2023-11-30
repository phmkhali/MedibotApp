import tkinter as tk
from tkinter import ttk
from db import get_requests

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

        self.left_frame = tk.Frame(self.mainframe, width=350, height=400) 
        self.left_frame.pack(fill='both', side='left', pady=40, padx=(60,0))
        
        self.right_frame = tk.Frame(self.mainframe)

        # tree
        style = ttk.Style()
        style.configure("Treeview.Heading", background="#a0a9de", foreground="black")
        style.configure("Treeview", foreground="black", rowheight=25, fieldbackground="#d3d3d3")
        
        # request from db
        request_as_List = get_requests()
        # requested with status 'requested'
        requested_requests = [request for request in request_as_List if request.status == "requested"]
        
        # Configure selected item color
        style.map("Treeview", background=[("selected", "#8c94c6")])
        
        tree = ttk.Treeview(self.left_frame, columns=("Medication", "Quantity", "Room"), show="headings")
        tree.heading("Medication", text="Medication")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Room", text="Room")
        
        tree.column("Medication", width=150, stretch=False) 
        tree.column("Quantity", width=100, stretch=False)
        tree.column("Room", width=100, stretch=False)  

        #todo "wenn man drauf klickt!" Daten aus der Datenbank löschen damit da nicht so komische werte auftreten
        #Also zum beispiel als auskommentierte methode in db
        # Add data to the treeview
        for request in requested_requests:
            tree.insert("", tk.END, values=(request.med_name, request.quantity, request.location, request.user))

        tree.pack(expand=True, fill='both')
        tree.bind("<<TreeviewSelect>>", self.on_select)

        self.med_qty_label = ttk.Label(self.right_frame, text="")
        self.med_qty_label.pack(padx=10,pady=(10,0))
        
        self.location_label = ttk.Label(self.right_frame, text="")
        self.location_label.pack()
        
        self.request_from_label = ttk.Label(self.right_frame, text="")
        self.request_from_label.pack()

        self.right_frame.rowconfigure(1, weight=1)
        
        # submit button
        submit_button = tk.Button(self.right_frame,  relief='flat', background='#4C4273', foreground='white', width='12', text="Submit", command=lambda text=button_text: self.button_click(text, switch_frame) )
        submit_button.pack(side='bottom', pady=10)  

    def on_select(self, event):
        self.med_qty_label["text"] = ""
        self.location_label["text"] = ""
        self.request_from_label["text"] = ""
        selection = event.widget.selection()

        if selection:
            selected_item = event.widget.item(selection, 'values')
            
            # to do: add unit
            self.med_qty_label["text"] = f"Selected Item: {selected_item[1]} {selected_item[0]}"
            self.location_label["text"] = f"Send to: {selected_item[2]}"
            self.request_from_label["text"] = f"Request from: {selected_item[3]}"
        
            self.right_frame.pack(side='right', pady=40, padx=(80,60), fill='both', expand=True) 
        else:
            self.right_frame.pack_forget()

    def button_click(self, button_text, switch_frame):
        if button_text == 'Request Robot':
            switch_frame('Request Robot')
        elif button_text == 'Home':
            switch_frame('Home')
        elif button_text == "Submit": 
            pass #hier dann die progess bar!
    
    
    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6' 

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de' 