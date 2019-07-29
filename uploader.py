import pyrebase

config = {
  "apiKey": "AIzaSyA_DnCX4WVdkQldH974rK31x-3N_WL6xqY",
  "authDomain": "techromancer-eba83.firebaseapp.com",
  "databaseURL": "https://techromancer-eba83.firebaseio.com",
  "storageBucket": "techromancer-eba83.appspot.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage();

upload_file1 = "test_dir/test.txt"
upload_file2 = "test_dir/home-left copy.png"
# "test_dir/home-left copy.png"
# "test_dir/test.txt";
# as admin
storage.child(user_data).put(upload_file1)
storage.child(user_data).put(upload_file2)
