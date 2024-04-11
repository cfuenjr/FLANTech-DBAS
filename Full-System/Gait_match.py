import keras
import numpy as np
from numpy.linalg import norm
import pickle
import CNN_features


def cosine_similarity(a, b):
    return np.dot(a, b) / (norm(a) * norm(b))


# # Load and prepare your dataset
# image_folder = './Silh_R'
# model = keras.models.load_model('./CNN_Model/model.keras')
# person = CNN_features.get_feature(image_folder)
#
# with open('feature_vectors.pkl', 'rb') as f:
#     data = pickle.load(f)
#
# # Determine the maximum array length, including the new 'person' vector
# max_length = max(max(len(value) for value in data.values()), len(person))
#
# # Pad each array in the data dictionary to match the maximum length
# padded_data = {key: CNN_features.pad_array(value, max_length) for key, value in data.items()}
# person_padded = CNN_features.pad_array(person, max_length)
#
# similarities = {key: cosine_similarity(value, person_padded) for key, value in padded_data.items()}
#
# print(similarities)
