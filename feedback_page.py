import tkinter as tk
from tkinter import ttk
from db import get_requests_with_status_delivering, get_requests_with_status_delivered, get_current_user_email, update_request_status_to_delivered, add_feedback
from tkinter import messagebox
from navbar import create_navbar

class FeedbackPage:
    def __init__(self, root, switch_frame):
        self.root = root
        self.mainframe = tk.Frame(self.root, bg='#333333')
        self.mainframe.pack(expand=True, fill='both')
        self.mainframe.columnconfigure(0, weight=1)

        # update every 5 seconds
        self.root.after(5000, self.update_feedback)

        # Navigation Bar-------------------------------------------------------------------------- 
        create_navbar(self.mainframe, switch_frame)

        # Page Content-------------------------------------------------------------------------- 
        self.left_frame = tk.Frame(self.mainframe, width=350, height=400, background='#333333')
        self.right_frame = tk.Frame(self.mainframe, width=350, height=400, background='#333333')

        self.update_feedback()

    # Methods --------------------------------------------------------------------------
    def show_messagebox(self):
        self.switch_frame("Home")   
        messagebox.showinfo("Confirmation", "Order delivered successfully.")
   
    def update_feedback(self):
        # Get requests for the current user
        active_requests = get_request_delivering_for_current_user()
        self.finished_requests = get_request_delivered_for_current_user()

        # Remove the existing left frame content
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        # Create the widgets outside the if condition
            
        # manually set status to delivered
        self.test_button = tk.Button(self.left_frame, text="set status to delivered", background='yellow', relief='flat', foreground='black', width=20, command=lambda: test(self,active_requests[0]))
        self.test_button.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.select_title_label = tk.Label(self.left_frame, text="Order Summary", background='#333333', foreground='white')
        self.select_title_label.config(font=("TkDefaultFont", 12, "bold"))
        
        self.medication_label = tk.Label(self.left_frame, text="Medication", background='#333333', foreground='white')
        self.quantity_label = tk.Label(self.left_frame, text="Quantity", background='#333333', foreground='white')
        self.location_label = tk.Label(self.left_frame, text="Location", background='#333333', foreground='white')
        self.patient_label = tk.Label(self.left_frame, text="Patient", background='#333333', foreground='white')
        self.status_label = tk.Label(self.left_frame, text="Status: currently delivering..", background='#333333', foreground='white')

        self.order_received_button = tk.Button(self.left_frame, text="Order received", background='#4C4273', relief='flat', foreground='white', width=15, command=lambda: self.show_messagebox())
        self.order_missing_button = tk.Button(self.left_frame, text="Order missing", background='#E83C3C', relief='flat', foreground='white', width=15, command=lambda: self.show_missing_order_content())

        if active_requests:
            # populate the left frame with current_order
            self.select_title_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
            self.medication_label.grid(row=1,column=0,padx=10, pady=(5,0), sticky='w')
            self.quantity_label.grid(row=2,column=0,padx=10, pady=(5,0), sticky='w')
            self.location_label.grid(row=3,column=0,padx=10, pady=(5,0), sticky='w')
            self.patient_label.grid(row=4,column=0,padx=10, pady=(5,0), sticky='w')
            self.status_label.grid(row=5,column=0,padx=10, pady=30, sticky='w')
            
            update_labels(self,active_requests[0])
                 
        elif self.finished_requests:
            self.select_title_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
            self.medication_label.grid(row=1,column=0,padx=10, pady=(5,0), sticky='w')
            self.quantity_label.grid(row=2,column=0,padx=10, pady=(5,0), sticky='w')
            self.location_label.grid(row=3,column=0,padx=10, pady=(5,0), sticky='w')
            self.patient_label.grid(row=4,column=0,padx=10, pady=(5,0), sticky='w')
            self.status_label.grid(row=5,column=0,padx=10, pady=30, sticky='w')

            self.order_received_button.grid(row=6,column=0,padx=10, pady=(5,0), sticky='w')
            self.order_missing_button.grid(row=7,column=0,padx=10, pady=(5,0), sticky='w')
            self.status_label.config(text='Status: delivered')

            update_labels(self,self.finished_requests[0])

        # if no requests are being worked on
        else:
            empty_label = tk.Label(self.left_frame, text="None of your orders are currently delivering.", background='#333333', foreground='white')
            empty_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
                        
        self.left_frame.pack(fill='both', side='left', pady=60, padx=(60, 0))

        # next update after 5 seconds
        self.root.after(5000, self.update_feedback)

    def show_messagebox(self):
        messagebox.showinfo("Confirmation", "Order delivered successfully.")
        self.switch_frame("Home")

    def show_missing_order_content(self):
        # Remove existing widgets in the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Radiobutton style
        style = ttk.Style()
        style.configure('TRadiobutton', background='#333333',foreground='white')
        
        # Medibot_arrived
        self.var = tk.StringVar()  # Variable for the Radiobutton
        arrived_label = tk.Label(self.right_frame, text="Has the Medibot arrived?", background='#333333',
                                 foreground='white')
        arrived_label.grid(row=0, column=0, padx=10, pady=(5, 0), sticky='w')

        yes_arrived = ttk.Radiobutton(self.right_frame, text="Yes", variable=self.var, value="Yes", style='TRadiobutton',
                                     command=self.on_radiobutton_click)
        yes_arrived.grid(row=1, column=0, padx=10, pady=(5, 0), sticky='w')

        no_arrived = ttk.Radiobutton(self.right_frame, text="No", variable=self.var, value="No", style='TRadiobutton',
                                    command=self.on_radiobutton_click)
        no_arrived.grid(row=1, column=1, padx=10, pady=(5, 0), sticky='w')

        # Medication_arrived
        self.var2 = tk.StringVar()  # Variable for the Radiobutton
        arrived_label = tk.Label(self.right_frame, text="Has all the medication arrived?", background='#333333',
                                 foreground='white')
        arrived_label.grid(row=2, column=0, padx=10, pady=(5, 0), sticky='w')

        yes_arrived = ttk.Radiobutton(self.right_frame, text="Yes", variable=self.var2, value="Yes",style='TRadiobutton',
                                     command=self.on_radiobutton_click2)
        yes_arrived.grid(row=3, column=0, padx=10, pady=(5, 0), sticky='w')

        no_arrived = ttk.Radiobutton(self.right_frame, text="No", variable=self.var2, value="No",style='TRadiobutton',
                                    command=self.on_radiobutton_click2)
        no_arrived.grid(row=3, column=1, padx=10, pady=(5, 0), sticky='w')

        information_label = tk.Label(self.right_frame, text="Please provide more information:", background='#333333',
                                     foreground='white')
        information_label.grid(row=4, column=0, padx=10, pady=(30, 0), sticky='w')

        self.more_information_entry = tk.Entry(self.right_frame)
        self.more_information_entry.grid(row=5, column=0, padx=10, pady=(5, 0), sticky='w')

        send_feedback_button = tk.Button(self.right_frame, relief='flat', background='#4C4273', text="Send Feedback",
                                         foreground='white', width='15', command=lambda: self.send_feedback_button())
        send_feedback_button.grid(row=6, column=0, padx=10, pady=(20, 0), sticky='w')

        # Pack the right frame into the mainframe
        self.right_frame.pack(fill='both', side='right', pady=60, padx=(0, 60))

    def on_radiobutton_click(self):
        selected_option = self.var.get()
        print("Selected Option:", selected_option)

    def on_radiobutton_click2(self):
        selected_option = self.var2.get()
        print("Selected Option:", selected_option)

        
    def send_feedback_button(self):
        entered_text = self.more_information_entry.get()
        selected_option1 = self.var.get()
        selected_option2 = self.var2.get()

        # Add feedback with selected options and entered text
        add_feedback(self.finished_requests[0], selected_option1, selected_option2, entered_text)

        # Clear selected options and text entry
        self.var.set("") 
        self.var2.set("")  
        self.more_information_entry.delete(0, tk.END)  

        self.right_frame.pack_forget()
        self.update_feedback()
        
        # success box
        messagebox.showinfo("Confirmation", "Feedback sent. Thanks for your help!")
        self.switch_frame('Request Robot')
        

def test(self, request):
    update_request_status_to_delivered(request)

def get_request_delivering_for_current_user():
    current_user = get_current_user_email()
    user_requests_delivering = get_requests_with_status_delivering(current_user)
    return user_requests_delivering

def get_request_delivered_for_current_user():
    current_user = get_current_user_email()
    user_requests_delivered = get_requests_with_status_delivered(current_user)
    return user_requests_delivered

def update_labels(self, request):
    self.medication_label["text"] = f"{request.med_name}"
    self.quantity_label["text"] = f"{request.quantity}"
    self.location_label["text"] = f"{request.location}"
    self.patient_label["text"] = f"{request.patientName}"
                    
# show currently processed order


        