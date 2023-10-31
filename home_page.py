import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, root, switch_frame):
        self.mainframe = tk.Frame(root, bg='#333333')
        self.mainframe.pack(expand=True)

        # Home Page Label
        home_label = ttk.Label(self.mainframe, text='Medibot Home', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 14))
        home_label.grid(row=0, column=0, pady=20)

        # Back to Login Button
        back_button = tk.Button(self.mainframe, text='Back to Login', background='#a087c7', border=0, foreground='white', command=lambda: switch_frame("Login"))
        back_button.grid(row=1, column=0, pady=20, padx=20, sticky='nswe')