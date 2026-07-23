import pickle
from pathlib import Path


def save_vocabulary(note_to_int, int_to_note):

    Path("data").mkdir(exist_ok=True)

    with open("data/note_to_int.pkl", "wb") as f:
        pickle.dump(note_to_int, f)

    with open("data/int_to_note.pkl", "wb") as f:
        pickle.dump(int_to_note, f)

    print("Vocabulary saved successfully!")


def load_vocabulary():

    with open("data/note_to_int.pkl", "rb") as f:
        note_to_int = pickle.load(f)

    with open("data/int_to_note.pkl", "rb") as f:
        int_to_note = pickle.load(f)

    return note_to_int, int_to_note