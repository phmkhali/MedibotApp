import tkinter as tk
from tkinter import ttk
from db import get_requests

class PendingRequestsPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.current_page = 'Pending Requests'
        
        # update every 5 seconds
        self.root.after(5000, self.update_tree)

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
        style.map("Treeview", background=[("selected", "#8c94c6")])
        
        self.tree = ttk.Treeview(self.left_frame, columns=("Medication", "Quantity", "Room"), show="headings")
        self.tree.heading("Medication", text="Medication")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Room", text="Room")
        
        self.tree.column("Medication", width=150, stretch=False) 
        self.tree.column("Quantity", width=100, stretch=False)
        self.tree.column("Room", width=100, stretch=False)  

        self.fill_tree()
        self.tree.pack(expand=True, fill='both')
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.med_qty_label = ttk.Label(self.right_frame, text="")
        self.med_qty_label.pack(padx=10,pady=(10,0))
        
        self.location_label = ttk.Label(self.right_frame, text="")
        self.location_label.pack()
        
        self.patient_name_label = ttk.Label(self.right_frame, text="")
        self.patient_name_label.pack()
        
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
        self.patient_name_label["text"] = ""
        selection = event.widget.selection()

        if selection:
            selected_item = event.widget.item(selection, 'values')
            
            # to do: add unit
            self.med_qty_label["text"] = f"Selected Item: {selected_item[1]} {selected_item[0]}"
            self.location_label["text"] = f"Send to: {selected_item[2]}"
            self.patient_name_label["text"] = f"Patient: {selected_item[3]}"
            self.request_from_label["text"] = f"Request from: {selected_item[4]}"
        
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
        
    # tree methods
    def update_tree(self):
        # get selected item before updating the tree
        selection = self.tree.selection()
        selected_item = None
        if selection:
            selected_item = self.tree.item(selection[0], 'values')
        
        # update the tree
        self.fill_tree()
        
        # reselect the item after update
        if selected_item:
            for item in self.tree.get_children():
                if self.tree.item(item, 'values') == selected_item:
                    self.tree.selection_set(item)
                    break
                
        # next update
        self.root.after(5000, self.update_tree)
        
    def fill_tree(self):
        # request from db
        all_requests = get_requests()
        # requested with status 'requested'
        requests_with_requested_status = [request for request in all_requests if request.status == "requested"]
        
        # clear existing items in the tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for request in requests_with_requested_status:
            self.tree.insert("", tk.END, values=(request.med_name, request.quantity, request.location, request.patientName, request.user))