import tkinter as tk
from tkinter import messagebox

class FeedbackPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.mainframe.columnconfigure(0, weight=1)
        self.switch_frame = switch_frame
        self.current_page = 'Feedback'

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
        self.left_frame = tk.Frame(self.mainframe, width=350, height=400, background='#333333')
        self.right_frame = tk.Frame(self.mainframe)

        # Update only the left frame with "Danke für eure Aufmerksamkeit!"
        self.update_thank_you_message()


    # Methods --------------------------------------------------------------------------

    def update_thank_you_message(self):
        # Remove the existing left frame content
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        # Display the thank you message
        thank_you_label = tk.Label(self.left_frame, text="2 + 2 = 5", background='#333333', foreground='white')
        thank_you_label.config(font=("TkDefaultFont", 35, "bold"))  
        thank_you_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.left_frame.pack(fill='both', side='left', pady=60, padx=(60, 0))

        # next update after 5 seconds
        self.root.after(5000, self.update_thank_you_message)

    def button_click(self, button_text, switch_frame):
        if button_text == 'Request Robot':
            switch_frame('Request Robot')
        elif button_text == 'Home':
            switch_frame('Home')
        elif button_text == 'Pending Requests':
            switch_frame('Pending Requests')
        elif button_text == 'Feedback':
            switch_frame('Feedback')
        elif button_text == "Confirm":
            pass

    def on_button_hover(self, event):
        event.widget['background'] = '#8c94c6'

    def on_button_leave(self, event):
        event.widget['background'] = '#a0a9de'

if __name__ == "__main__":
    # Example of how to use the FeedbackPage class
    root = tk.Tk()
    switch_frame = lambda frame_name: print(f"Switching to {frame_name}")
    feedback_page = FeedbackPage(root, switch_frame)
    root.mainloop()
