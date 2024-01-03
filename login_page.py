import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db import create_user, sign_in

class LoginPage:
    def __init__(self, root, switch_frame):
        
        self.mainframe = tk.Frame(root, bg='#333333')
        self.mainframe.pack(expand=True)

        self.header_label = ttk.Label(self.mainframe, text='Medibot', background='#333333', foreground='#a087c7', font=("Microsoft YaHei UI Bold", 50))
        self.header_label.grid(row=0, column=0, columnspan=2, pady=(0, 30), padx=20)

        # Entry fields -------------------------------------------------------------------------- 
        self.username_label = ttk.Label(self.mainframe, text='Username', background='#333333', foreground='white')
        self.username_label.grid(row=1, column=0, padx=20, sticky='w')
        self.username_text_field = ttk.Entry(self.mainframe,width=20)
        self.username_text_field.grid(row=1, column=1, padx=10, sticky='e')

        self.password_label = ttk.Label(self.mainframe, text='Password', background='#333333', foreground='white')
        self.password_label.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.password_text_field = ttk.Entry(self.mainframe, show="*",width=20)
        self.password_text_field.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        # Login Button -------------------------------------------------------------------------- 
        login_button = tk.Button(self.mainframe, text='Login', relief='flat', background='#4C4273', foreground='white', width='12', command=lambda: self.check_credentials(switch_frame))
        login_button.grid(row=3, column=0, pady=10, padx=20, sticky='w')

    # Functions -------------------------------------------------------------------------- 
    def check_credentials(self, switch_frame):
        username = self.username_text_field.get()
        password = self.password_text_field.get()
        #if username == "admin" and password == "admin":
        #    switch_frame("Home")
        #else:
        #    messagebox.showerror("Login Error", "Invalid username or password")
        #self.clear_fields()
        if username == "" or password == "":
            messagebox.showerror("Login Error", "Invalid username or password")
        else:
            user_id = sign_in(email = username, password = password)
            if user_id:
                switch_frame("Home")
            else:
                messagebox.showerror("Login Error", "Invalid username or password")                 
            self.clear_fields()                                      
            
    def clear_fields(self):
        self.username_text_field.delete(0, 'end')
        self.password_text_field.delete(0, 'end')