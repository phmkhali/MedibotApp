import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from main import logout

class HomePage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')

        self.current_page = 'Home'
        self.switch_frame = switch_frame

        # Navigation Bar-------------------------------------------------------------------------- 
        navbar_frame = tk.Frame(self.mainframe, background='#a0a9de')
        navbar_frame.pack(fill='x')

        buttons = ['Home', 'Request Robot', 'Pending Requests', 'Feedback', 'Config']
        self.nav_buttons = []
        for button_text in buttons:
            if button_text == self.current_page:
                button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text), bg='#8c94c6', bd=0)
            else:
                button = tk.Button(navbar_frame, text=button_text, command=lambda text=button_text: self.button_click(text), bg='#a0a9de', bd=0)
            button.config(height=4) 
            button.pack(side='left', fill='both', expand=True)
            self.nav_buttons.append(button)
            button.bind("<Enter>", self.on_button_hover)  # hover event
            button.bind("<Leave>", self.on_button_leave)  # leave event

        # Home Page Content-------------------------------------------------------------------------- 
        left_frame = tk.Frame(self.mainframe, width=300, background='#333333')
        left_frame.pack(fill='y', side='left', pady=(150,0), padx=(60,0))

        right_frame = tk.Frame(self.mainframe, background='#333333', width=400)
        right_frame.pack(fill='both', expand=True, side='right', pady=20, padx=40)

        home_label = ttk.Label(left_frame, text='Medibot', background='#333333', foreground='white', font=("Microsoft YaHei UI Bold", 45))
        home_label.grid(row=0, column=0, pady=10, sticky='w')

        select_robot = tk.Label(left_frame, text="Select Medibot", background='#333333', foreground='white')
        select_robot.grid(row=1, column=0, pady=10, sticky='w') 

        options = ['Medibot 1', 'Medibot 2', 'Medibot 3']  # todo: Medibot connection
        self.selected_option = tk.StringVar()
        medibot_dropdown = ttk.OptionMenu(left_frame, self.selected_option, *options)
        medibot_dropdown.config(width=25)
        medibot_dropdown.grid(row=2, column=0, pady=10, sticky='w') 

        connect_button = tk.Button(left_frame, relief='flat', background='#4C4273', foreground='white', text='Connect', width='12')
        connect_button.grid(row=3, column=0, pady=10, sticky='w')

        # Status
        self.status_indicator = ttk.Label(left_frame, text='', background='#333333', foreground='white')
        self.status_indicator.grid(row=4, column=0, pady=40, sticky='w')
        self.update_status('connected')  # Initial status

        # Right side
        right_frame.grid_columnconfigure(0, weight=1)
        logout_button = tk.Button(right_frame, relief='flat', background='#E83C3C', text='Log out', width='12', command=lambda: self.switch_frame('Login'))
        logout_button.grid(row=0, column=0, pady=20, sticky='ne')

        # Map
        image = PhotoImage(file="example_map.png")
        image_label = tk.Label(right_frame, image=image)
        image_label.grid(pady=20, row=1, column=0)

    def update_status(self, status):
        if status == 'connected':
            self.status_indicator.config(text='Status: Medibot 1 connected') 
        else:
            self.status_indicator.config(text='Status: disconnected')

    def button_click(self, button_text):
        self.current_page = button_text  
        for button in self.nav_buttons:
            if button.cget('text') == button_text:
                button['background'] = '#8c94c6'
            else:
                button['background'] = '#a0a9de'

        if button_text == 'Home':
            self.switch_frame('Home')
        elif button_text == 'Log out':
            logout()  
        elif button_text == 'Request Robot':
            self.switch_frame('Request Robot')
        elif button_text == 'Pending Requests':
            self.switch_frame('Pending Requests')  
        else:
            self.switch_frame(button_text)

    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6'

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de'

if __name__ == '__main__':
    root = tk.Tk()
    app = HomePage(root, lambda frame: print(f"Switching to {frame}"))
    root.mainloop()
