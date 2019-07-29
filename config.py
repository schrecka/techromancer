import pyrebase

# var firebaseConfig = {
#     apiKey: "AIzaSyA_DnCX4WVdkQldH974rK31x-3N_WL6xqY",
#     authDomain: "techromancer-eba83.firebaseapp.com",
#     databaseURL: "https://techromancer-eba83.firebaseio.com",
#     projectId: "techromancer-eba83",
#     storageBucket: "techromancer-eba83.appspot.com",
#     messagingSenderId: "1074095214566",
#     appId: "1:1074095214566:web:0d09751eee5bbbde"
#   };
#   // Initialize Firebase
#   firebase.initializeApp(firebaseConfig);

config = {
  "apiKey": "AIzaSyA_DnCX4WVdkQldH974rK31x-3N_WL6xqY",
  "authDomain": "techromancer-eba83.firebaseapp.com",
  "databaseURL": "https://techromancer-eba83.firebaseio.com",
  "storageBucket": "techromancer-eba83.appspot.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage();
storage.child("user_data")
