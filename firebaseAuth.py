from firebase_admin import credentials

cred_obj = firebase_admin.credentials.Certificate('....path to file')
default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL':databaseURL
	})


# ================================================
# from pyfirebase import Firebase
# from flask import session


# firebaseConfig = {
#     'apiKey': "AIzaSyAQtgeFPMP-ux3TxvecLxtsdJbjh_hcCAs",
#     'authDomain': "digital-identity-creation.firebaseapp.com",
#     'projectId': "digital-identity-creation",
#     'storageBucket': "digital-identity-creation.appspot.com",
#     'messagingSenderId': "724974146763",
#     'appId': "1:724974146763:web:23e86d8b048b37ac78774e",
#     'measurementId': "G-BTBBQKT652"
# }

# firebase = Firebase(api_key=firebaseConfig['apiKey'],
#                     auth_domain=firebaseConfig['authDomain'],
#                     database_url="https://" + firebaseConfig['projectId'] + ".firebaseio.com",
#                     storage_bucket=firebaseConfig['storageBucket'])
# auth = firebase.auth()

# def login(email, password):
#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         session['logged_in'] = True
#         session['user_id'] = user['localId']
#         return True
#     except:
#         return False
# ===============================================================

# # import pyrebase
# from flask import session

# firebaseConfig = {
#     'apiKey': "AIzaSyAQtgeFPMP-ux3TxvecLxtsdJbjh_hcCAs",
#     'authDomain': "digital-identity-creation.firebaseapp.com",
#     'projectId': "digital-identity-creation",
#     'storageBucket': "digital-identity-creation.appspot.com",
#     'messagingSenderId': "724974146763",
#     'appId': "1:724974146763:web:23e86d8b048b37ac78774e",
#     'measurementId': "G-BTBBQKT652"
# }

# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()

# def login(email, password):
#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         session['logged_in'] = True
#         session['user_id'] = user['localId']
#         return True
#     except:
#         return False

