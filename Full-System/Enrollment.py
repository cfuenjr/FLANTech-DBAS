from userClass import Entry
import numpy as np
import pickle


def enroll(class_obj):
    # Initialize Variables
    #count = 1

    # Load data_dict from .pkl database
    with open('database.pkl', 'rb') as f:
        data_dict = pickle.load(f)

    # Find new index number
    #for key in data_dict.items():
        #count += 1
    username = input("Input name of user: ")
    # Append data_dict
    data_dict[username] = class_obj
    # for value in data_dict.values():
    #     print(value.gait90)

    # Overwrite .pkl database
    with open('database.pkl', 'wb') as f:
        pickle.dump(data_dict, f)

    return username
