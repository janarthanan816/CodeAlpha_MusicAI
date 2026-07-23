import numpy as np

def prepare_training_data(encoded_notes, sequence_length):
    """
    Convert encoded notes into X and y.
    """

    X = []
    y = []

    for i in range(len(encoded_notes) - sequence_length):

        X.append(encoded_notes[i:i+sequence_length])

        y.append(encoded_notes[i+sequence_length])

    return np.array(X), np.array(y)