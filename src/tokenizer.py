def build_vocabulary(notes):
    """
    Create mappings between notes and integers.
    """

    unique_notes = sorted(set(notes))

    note_to_int = {}
    int_to_note = {}

    for index, note in enumerate(unique_notes):
        note_to_int[note] = index
        int_to_note[index] = note

    return note_to_int, int_to_note


def encode_notes(notes, note_to_int):
    """
    Convert notes into integers.
    """

    encoded_notes = []

    for note in notes:
        encoded_notes.append(note_to_int[note])

    return encoded_notes