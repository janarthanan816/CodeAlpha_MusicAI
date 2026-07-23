from config import SEQUENCE_LENGTH

def create_sequences(notes):
    """
    Create input-output sequences from a list of notes.
    """

    inputs = []
    outputs = []

    for i in range(len(notes) - SEQUENCE_LENGTH):

        input_sequence = notes[i:i + SEQUENCE_LENGTH]
        output_note = notes[i + SEQUENCE_LENGTH]

        inputs.append(input_sequence)
        outputs.append(output_note)

    return inputs, outputs