import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title('Medibot')
        self.root.resizable(False, False)

        self.frames = {}

        self.create_frames()
        self.show_frame("Login")

        self.root.mainloop()

    def create_frames(self):
        for frame_name in ["Login", "Home"]:
            frame = tk.Frame(self.root, bg='#333333')
            self.frames[frame_name] = frame

        LoginPage(self.frames["Login"], self.show_frame)
        HomePage(self.frames["Home"], self.show_frame)

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill='both', expand=True)
        

class LoginPage:
    def __init__(self, root, switch_frame):

        self.mainframe = tk.Frame(root, bg='#333333')
        self.mainframe.pack(expand=True)

        # Header Label
        self.header_label = ttk.Label(self.mainframe, text='Medibot', background='#333333', foreground='#a087c7', font=("Microsoft YaHei UI Light", 50))
        self.header_label.grid(row=0, column=0, columnspan=2, pady=(0, 30), padx=20)

        # Username Label and Entry
        self.username_label = ttk.Label(self.mainframe, text='Username', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 14))
        self.username_label.grid(row=1, column=0, padx=20, sticky='w')
        self.username_text_field = ttk.Entry(self.mainframe)
        self.username_text_field.grid(row=1, column=1, padx=10, sticky='e')

        # Password Label and Entry
        self.password_label = ttk.Label(self.mainframe, text='Password', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 14))
        self.password_label.grid(row=2, column=0, padx=20, pady=5, sticky='w')
        self.password_text_field = ttk.Entry(self.mainframe, show="*")
        self.password_text_field.grid(row=2, column=1, padx=10, sticky='e')

        # Login Button
        login_button = tk.Button(self.mainframe, text='Login', background='#a087c7', border=0, foreground='white', command=lambda: switch_frame("Home"))
        login_button.grid(row=3, column=0, pady=20, padx=20, sticky='nswe')

class HomePage:
    def __init__(self, root, switch_frame):
        self.mainframe = tk.Frame(root, bg='#333333')
        self.mainframe.pack(fill='both', expand=True)

        # Home Page Label
        home_label = ttk.Label(self.mainframe, text='Welcome to the Home Page', background='#333333', foreground='white', font=("Microsoft YaHei UI Light", 14))
        home_label.grid(row=0, column=0, padx=20, pady=20)

        # Back to Login Button
        back_button = tk.Button(self.mainframe, text='Back to Login', background='#a087c7', border=0, foreground='white', command=lambda: switch_frame("Login"))
        back_button.grid(row=1, column=0, pady=20, padx=20, sticky='nswe')

if __name__ == '__main__':
    App()
