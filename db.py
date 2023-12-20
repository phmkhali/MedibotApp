import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import firestore
from firebase_admin.exceptions import FirebaseError
from request import Request
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
current_user = ''

#db.collection('medications').add({'name':'paracetamol', 'dose':400})

#Authentication
def sign_in(email, password):
    global current_user # global variable
    try:
        user = auth.get_user_by_email(email)
        print('Successfully signed in as:', user.uid)
        current_user = email
        return user.uid
    #except auth.AuthError as e:
    except FirebaseError as e:
       # print('Error signing in':, e)
        return None

#create user
def create_user(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print('Successfully created user:', user.uid)
        return user.uid
   # except firebase_admin.auth.AuthError as e:
    except FirebaseError as e:
        print('Error creating user:', e)
        return None
    
def get_current_user_email():
    return current_user


# get meds from db
def get_medication_db():
    medications_ref = db.collection("medication")
    medications = medications_ref.stream()
    
    medication_names = []  # List to store the medication names
    medication_info = {}  # Dictionary to store the medication information

    for med in medications:
        med_data = med.to_dict()
        name = med_data.get("name")
        unit = med_data.get("unit")

        # Create a dictionary with all the information
        med_dict = {
            "name": name,
            "unit": unit,
        }

        # Store the dictionary in the overall medication_info dictionary
        medication_info[name] = med_dict

        # Append the name to the list
        medication_names.append(name)

    return medication_names, medication_info

# create request from request_robot_page
def create_request(location, medName, quantity, patientName):
    
    new_request_ref = db.collection('request').add({
        'location': location,
        'medName': medName,
        'quantity': quantity,
        'patientName': patientName,
        'user': current_user,
        'status': 'requested'
    })
    
    # get doc_id from firebase
    document_id = new_request_ref[1].id
    new_request_ref[1].update({'fire_id': document_id})

    
def clear_requests():
    try:
        requests_ref = db.collection("request")
        requests = requests_ref.stream()

        for request_doc in requests:
            request_doc.reference.delete()

        print('All requests successfully deleted.')
    except FirebaseError as e:
        print('Error clearing database:', e)

# update request status after submitting in pending_request
def update_request_status_to_currently_delivering(request):
    request_ref = db.collection("request").document(request.fire_id)
    request.status = "currently delivering"
    request_ref.update({ "status": "currently delivering" })

def update_request_status_to_delivered(request):
    request_ref = db.collection("request").document(request.fire_id)
    request.status = "delivered"
    request_ref.update({ "status": "delivered" })

def update_request_status_to_failed(request):
    request_ref = db.collection("request").document(request.fire_id)
    request.status = "failed"
    request_ref.update({ "status": "failed" })    
    
def add_feedback(request, medibot_arrived, medication_arrived, information_text):
    sammlung_referenz = db.collection("feedback").add({
        'request_id':request.fire_id,
        'medibot_arrived':medibot_arrived,
        'medication_arrived':medication_arrived,
        'information_text':information_text
    })
    update_request_status_to_failed(request)
    

# get request from db
def get_requests():
    requests = db.collection("request").get()
    requests_list = []
    requests_list.clear()

    for request_doc in requests:
        request_data = request_doc.to_dict()

        request_instance = Request(
            medName=request_data.get("medName"),
            location=request_data.get("location"),
            quantity=request_data.get("quantity"),
            patientName=request_data.get("patientName"),
            user=request_data.get("user"),
            status=request_data.get("status"),
            fire_id=request_data.get("fire_id")
        )

        requests_list.append(request_instance)

    return requests_list

# generate feedback for delivering request
def get_requests_with_status_delivering(current_user):
    all_requests = get_requests()
    
    requests_with_currently_delivering_status = [request for request in all_requests if request.status == "currently delivering" and request.user == current_user]
    return requests_with_currently_delivering_status

def get_requests_with_status_delivered(current_user):
    all_requests = get_requests()
    
    requests_with_delivered_status = [request for request in all_requests if request.status == "delivered" and request.user == current_user]
    return requests_with_delivered_status

#create_user(email="smith@doctor.hos", password="123456")
#create_user(email="jones@doctor.hos", password="123456")
#create_user(email="holdt@interim.hos", password="qwert123")

def sign_out():
    try:
        firebase_admin.auth.sign_out()
        print('User successfully logged out.')
        current_user = ''
    except FirebaseError as e:
        print('Error logging out:', e)
