import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

class HomePage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        
        self.current_page = 'Home'

        # Navigation Bar-------------------------------------------------------------------------- 
        navbar_frame = tk.Frame(self.mainframe, background='#a0a9de')
        navbar_frame.pack(fill='x')

        buttons = ['Home', 'Request Robot', 'Pending Requests', 'Feedback', 'Config']
        self.nav_buttons = []
        for button_text in buttons:
            if button_text == self.current_page:
                button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text, switch_frame), bg='#8c94c6', bd=0)
            else:
                button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text, switch_frame), bg='#a0a9de', bd=0)
            button.config(height=4) 
            button.pack(side='left', fill='both', expand=True)
            self.nav_buttons.append(button)
            button.bind("<Enter>", self.on_button_hover)  # hover event
            button.bind("<Leave>", self.on_button_leave)  # leave event

        # Home Page Content-------------------------------------------------------------------------- 
        left_frame = tk.Frame(self.mainframe, width=300, background='#333333')
        left_frame.pack(fill='y', side='left', pady=20, padx=(60,0))
        
        logout_button = ttk.Button(self.mainframe,text='Log out')
        logout_button.pack(side='right', pady=20, padx=40)
        
        right_frame = tk.Frame(self.mainframe, background='#333333', width=400)
        right_frame.pack(side='right', pady=20, padx=40)
        
        home_label = ttk.Label(left_frame, text='Medibot', background='#333333', foreground='white', font=("Microsoft YaHei UI Bold", 45))
        home_label.grid(row=0,column=0,pady=(40,10),sticky='w')
        
        select_robot = tk.Label(left_frame, text="Select Medibot", background='#333333', foreground='white')
        select_robot.grid(row=1,column=0, pady=10,sticky='w') 

        options = ['Medibot 1', 'Medibot 2', 'Medibot 3'] #todo: Medibot connection
        self.selected_option = tk.StringVar()
        medibot_dropdown = ttk.OptionMenu(left_frame, self.selected_option, *options)
        medibot_dropdown.grid(row=2,column=0, pady=10,sticky='w') 
        
        connect_button = ttk.Button(left_frame, text='Connect')
        connect_button.grid(row=3,column=0, pady=10,sticky='w')

        # Status
        self.status_indicator = ttk.Label(left_frame, text='', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 18))
        self.status_indicator.grid(row=4, column=0,pady=(40,20), sticky='s')
        
        self.status_canvas = tk.Canvas(left_frame, width=20, height=20, background='#333333', bd=0, highlightthickness=0)
        self.status_canvas.grid(row=5, column=0, pady=20, sticky='s')
        self.status_canvas.create_oval(2, 2, 18, 18, fill='green', outline='#333333', tags="status_indicator") 
        self.update_status('connected')  # Initial status
        
                
        # Map
        image = PhotoImage(file="example_map.png")
        image_label = tk.Label(right_frame, image=image)
        image_label.pack(pady=20, anchor='center', expand=True)


    def update_status(self, status):
        if status == 'connected':
                self.status_indicator.config(text='Status: Medibot 1 connected')
                self.status_canvas.itemconfig("status_indicator", fill='green')  
        else:
                self.status_indicator.config(text='Status: disconnected')
                self.status_canvas.itemconfig("status_indicator", fill='red') 

    def button_click(self, button_text, switch_frame):
        self.current_page = button_text  
        for button in self.nav_buttons:
            if button.cget('text') == button_text:
                button['background'] = '#8c94c6'
            else:
                button['background'] = '#a0a9de'

        if button_text == 'Logout':
            # Logout Firebase
            switch_frame('Login')
        elif button_text == 'Home':
            switch_frame('Home')
        elif button_text == 'Request Robot':
            switch_frame('Request Robot')
        elif button_text == 'Pending Requests':
            switch_frame('Pending Requests')  
        else:
            self.switch_frame(button_text)
            
            
    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6'

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de'
