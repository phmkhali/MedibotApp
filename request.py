class Request:
    def __init__(self, medName, location, quantity, user, status):
        self.med_name = medName 
        self.location = location
        self.quantity = quantity
        self.user = user
        self.status = status
 

    def set_status_processing(self):
        self.status = "processing"

    def set_status_done(self):
        self.status = "done"