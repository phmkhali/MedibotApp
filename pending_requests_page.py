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

        self.left_frame = tk.Frame(self.mainframe, width=1200, background='#333333')
        self.left_frame.pack(fill='both', side='left', pady=20, padx=30)
        
        self.right_frame = tk.Frame(self.mainframe, width=600)
        self.right_frame.pack(fill='both', side='right', pady=20, padx=30)
        self.right_frame.pack_forget()

        requestsList = tk.Listbox(self.left_frame)
        requestsList.grid( row= 0, column= 0, padx=20 , pady= 20)
        requestsList.bind("<<ListboxSelect>>", self.on_select)
        # todo: Liste sinnvoll befüllen
        requestsList.insert(tk.END, "Paracetamol 500    2 Qty       Room 3") #zum Testen
        requestsList.insert(tk.END, "Paracetamol 500    1 Qty       Room 2")
        requestsList.insert(tk.END, "Calcium Sandoz 500 1 Qty       Room 2")

        self.Info_label = ttk.Label(self.right_frame , text="Here should be all the Information")
        self.Info_label.grid(row= 0, column=2, padx= 5, pady= 5, sticky=tk.N)
        
        self.right_frame.rowconfigure(1, weight=1)
        submit_button = ttk.Button(self.right_frame, text="Submit", command=lambda text=button_text: self.button_click(text, switch_frame) )
        submit_button.grid(row=5, column=2, padx=5, pady=5, sticky=tk.S)  


    def on_select(self, event):
        selected_item = event.widget.get(event.widget.curselection())
        #Je nachdem was in der Liste ist hier anpassen!
        self.Info_label["text"] = selected_item
        self.right_frame.pack(fill='both', side='right', pady=20, padx=30)

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