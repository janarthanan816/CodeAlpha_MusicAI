import pickle
from pathlib import Path

def save_notes(notes):

    Path("data").mkdir(exist_ok=True)

    with open("data/notes.pkl", "wb") as file:
        pickle.dump(notes, file)

    print("Notes saved successfully!")