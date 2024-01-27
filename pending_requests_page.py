import tkinter as tk
from tkinter import ttk
from db import get_requests, update_request_status_to_currently_delivering
from navbar import create_navbar

class PendingRequestsPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.current_page = 'Pending Requests'
        
        # update every 5 seconds
        self.root.after(5000, self.update_tree)

        # Navigation Bar-------------------------------------------------------------------------- 
        create_navbar(self.mainframe, switch_frame)
                
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
        submit_button = tk.Button(self.right_frame, relief='flat', background='#4C4273', text="Submit", foreground='white', width='12', command=lambda: self.submit_button(switch_frame))
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

     
    def submit_button(self, switch_frame):
        selection = self.tree.selection() 
        selected_item = None
        if selection:
            selected_item = self.tree.item(selection[0], 'values')
            
            all_requests = get_requests()
            corresponding_request_list = [request for request in all_requests if request.fire_id == selected_item[-1]]
            corresponding_request = corresponding_request_list[0]
            update_request_status_to_currently_delivering(corresponding_request)
            switch_frame("Feedback")
        
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

        # Sort the requests by room
        requests_with_requested_status = sorted(requests_with_requested_status, key=lambda x: x.location)

        # clear existing items in the tree
        for item in self.tree.get_children():
            self.tree.delete(item)

        # insert requests with 'requested'
        for request in requests_with_requested_status:
            self.tree.insert("", tk.END, values=(request.med_name, request.quantity, request.location, request.patientName, request.user, request.fire_id))
