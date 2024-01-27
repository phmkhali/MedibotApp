import tkinter as tk
from tkinter import ttk
from db import sign_out
from PIL import ImageTk, Image  
from navbar import create_navbar

class HomePage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')

        # Navigation Bar-------------------------------------------------------------------------- 
        create_navbar(self.mainframe, switch_frame)

        # Home Page Content-------------------------------------------------------------------------- 
        left_frame = tk.Frame(self.mainframe, width=300, background='#333333')
        left_frame.pack(fill='y', side='left', pady=(150,40), padx=(60,0),expand=True)

        right_frame = tk.Frame(self.mainframe, background='#333333', width=400)
        right_frame.pack(fill='both', expand=True, side='right', pady=40, padx=40)

        home_label = ttk.Label(left_frame, text='Medibot', background='#333333', foreground='white', font=("Microsoft YaHei UI Bold", 45))
        home_label.grid(row=0, column=0, pady=10, sticky='w')

        select_robot = tk.Label(left_frame, text="Select Medibot", background='#333333', foreground='white')
        select_robot.grid(row=1, column=0, pady=10, sticky='w') 

        options = ['Medibot 1', 'Medibot 2', 'Medibot 3']  # todo: Medibot connection
        self.selected_option = tk.StringVar()
        medibot_dropdown = ttk.OptionMenu(left_frame, self.selected_option, options[0],*options)
        medibot_dropdown.config(width=25)
        medibot_dropdown.grid(row=2, column=0, sticky='w') 
    
        connect_button = tk.Button(left_frame, relief='flat', background='#4C4273', foreground='white', text='Connect', width='12')
        connect_button.grid(row=3, column=0, pady=10, sticky='w')

        # Status
        self.status_indicator = ttk.Label(left_frame, text='', background='#333333', foreground='white')
        self.status_indicator.grid(row=4, column=0, pady=40, sticky='sw')
        self.update_status('connected')  # Initial status

        # Right side
        right_frame.grid_columnconfigure(0, weight=1)
        logout_button = tk.Button(right_frame, relief='flat', background='#E83C3C', text='Log out', width='12', command=lambda: self.switch_frame('Login'))
        logout_button.grid(row=0, column=0, pady=20, sticky='ne')

        # Map
        map_image_path = 'map.pgm'  
        self.map_image = ImageTk.PhotoImage(Image.open(map_image_path))
        map_label = tk.Label(right_frame, image=self.map_image, background='#333333')
        map_label.grid(row=1, column=0, pady=20, sticky='nsew')


    def update_status(self, status):
        if status == 'connected':
            self.status_indicator.config(text='Status: Medibot 1 connected') 
        else:
            self.status_indicator.config(text='Status: disconnected')

if __name__ == '__main__':
    root = tk.Tk()
    app = HomePage(root, lambda frame: print(f"Switching to {frame}"))
    root.mainloop()
