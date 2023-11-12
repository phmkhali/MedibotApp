import tkinter as tk
from tkinter import ttk

class PendingRequestsPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')



submit_button = ttk.Button(self.main_frame, text="Submit", command=submit)
submit_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)  

def submit():
    pass