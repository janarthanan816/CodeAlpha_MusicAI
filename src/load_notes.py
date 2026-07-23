import pickle

def load_notes():
    """
    Load the saved notes from disk.
    """

    with open("data/notes.pkl", "rb") as file:
        notes = pickle.load(file)

    print(f"Loaded {len(notes)} notes successfully!")

    return notes