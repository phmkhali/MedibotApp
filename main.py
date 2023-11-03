import tkinter as tk
from home_page import HomePage
from login_page import LoginPage
from send_robot_page import SendRobotPage
from feedback_page import FeedbackPage

class App:
    def __init__(self):
        # Main Window -------------------------------------------------------------------------- 
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title('Medibot')
        self.root.config(bg="#333333")
        self.root.resizable(False, False)

        self.frames = {}

        self.create_frames()
        self.show_frame("Home")

        self.root.mainloop()

    # Switch between windows -------------------------------------------------------------------------- 
    def create_frames(self):
        for frame_name in ["Login", "Home", "Send Robot", "Feedback"]:
            frame = tk.Frame(self.root, bg='#333333')
            self.frames[frame_name] = frame

        LoginPage(self.frames["Login"], self.show_frame)
        HomePage(self.frames["Home"], self.show_frame)
        SendRobotPage(self.frames["Send Robot"], self.show_frame)
        FeedbackPage(self.frames["Feedback"], self.show_frame)

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill='both', expand=True)

if __name__ == '__main__':
    App()
