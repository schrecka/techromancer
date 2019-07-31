import pyrebase
import re

def run():
    config = {
      "apiKey": "AIzaSyA_DnCX4WVdkQldH974rK31x-3N_WL6xqY",
      "authDomain": "techromancer-eba83.firebaseapp.com",
      "databaseURL": "https://techromancer-eba83.firebaseio.com",
      "storageBucket": "techromancer-eba83.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage();

    read_file = "logger.txt"
    file_changes = set()
    with open(read_file) as f:
        for x in f:
            #print(x.split(" ")[-1].rstrip())
            file_changes.add(x.split(" ")[-1].rstrip())

    #print(files)
    #upload_file2 = "test_dir/home-left copy.png"
    # "test_dir/home-left copy.png"
    # "test_dir/test.txt";
    # as admin

    for file in list(file_changes):
        #print(file)
        storage.child("user_data").child(file).put(file.strip())


    open(read_file, "w").close()
