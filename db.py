import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import firestore
from firebase_admin.exceptions import FirebaseError

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


#db.collection('medications').add({'name':'paracetamol', 'dose':400})


#Authentication
def sign_in(email, password):
    try:
        user = auth.get_user_by_email(email)
        print('Successfully signed in as:', user.uid)
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
    
def get_current_user():
    try:
        # Get the current user object
        user = firebase_admin.auth.get_user()

        # Extract and return the user's email
        return user.email

    except FirebaseError as e:
        print('Error getting current user:', e)
        return None


# get meds from db
def get_medication_db():
    medications_ref = db.collection("medication")
    medications = medications_ref.stream()

    medication_data = [{"medID": medication.id, "name": medication.to_dict()["name"]} for medication in medications]
    return medication_data


def get_medication_names():
    medications_ref = db.collection("medication")
    medications = medications_ref.stream()

    medication_names = [medication.to_dict()["name"] for medication in medications]
    return medication_names
    
#get request from db

def get_requests():
    requests = db.collection("request").where("status","==","requested").get()
    requests_dict = {}
    for item in requests:
        item_dict = item.to_dict()
        requests_dict[item.id] = item_dict
    return requests_dict


#create_user(email="smith@doctor.hos", password="123456")
#create_user(email="jones@doctor.hos", password="123456")

def sign_out():
    try:
        firebase_admin.auth.sign_out()
        print('User successfully logged out.')
    except FirebaseError as e:
        print('Error logging out:', e)
