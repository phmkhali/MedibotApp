import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, root, switch_frame):
        self.mainframe = tk.Frame(root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.mainframe.columnconfigure(0, weight=1)

        # Navigation Bar
        navigation_frame = tk.Frame(self.mainframe, bg='#a0a9de')
        navigation_frame.grid(row=0, column=0, sticky='nsew', columnspan=3)
        navigation_frame.columnconfigure(0, weight=1)

        # Button Formatting-------------------------------------------------------------------------- 
        button_style = ttk.Style()
        button_style.configure("TButton", foreground="black", background="#c7cdeb", font=("Microsoft YaHei UI Light", 12))

        button_texts = ['Home', 'Send Robot', 'Feedback', 'Scan Area', 'Logout']
        count_buttons = len(button_texts)

        button_width = int(600 / count_buttons)

        for i in range(count_buttons):
            navigation_frame.columnconfigure(i, weight=1)

        # Nav Buttons-------------------------------------------------------------------------- 
        home_button = ttk.Button(navigation_frame, text='Home', command=lambda: switch_frame("Home"))
        home_button.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        home_button.config(width=button_width, style="TButton")

        send_robot_button = ttk.Button(navigation_frame, text='Send Robot', command=lambda: switch_frame("Send Robot"))
        send_robot_button.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        send_robot_button.config(width=button_width, style="TButton")

        feedback_button = ttk.Button(navigation_frame, text='Feedback', command=lambda: switch_frame("Feedback"))
        feedback_button.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        feedback_button.config(width=button_width, style="TButton")        
        
        scan_area_button = ttk.Button(navigation_frame, text='Scan Area', command=lambda: switch_frame("Scan Area"))
        scan_area_button.grid(row=0, column=3, padx=10, pady=10, sticky='ew')
        scan_area_button.config(width=button_width, style="TButton")
        
        logout_button = ttk.Button(navigation_frame, text='Logout', command=lambda: switch_frame("Login"))
        logout_button.grid(row=0, column=4, padx=10, pady=10, sticky='ew')
        logout_button.config(width=button_width, style="TButton")

        # Home Page Content-------------------------------------------------------------------------- 
        home_label = ttk.Label(self.mainframe, text='Medibot Home', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 14))
        home_label.grid(row=1, column=0, pady=20)
        
        placeholder_label = ttk.Label(self.mainframe, text='Welcome to Medibot. This is the home page.', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 12))
        placeholder_label.grid(row=2, column=0, pady=20)
