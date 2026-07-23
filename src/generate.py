import random
import numpy as np
from tensorflow.keras.models import load_model

from load_notes import load_notes
from vocabulary import load_vocabulary
from config import SEQUENCE_LENGTH

print("=" * 50)
print("Loading Model...")
print("=" * 50)

model = load_model("models/music_generator.keras")

print("Model Loaded!")

notes = load_notes()

note_to_int, int_to_note = load_vocabulary()

encoded_notes = [note_to_int[n] for n in notes]

# Pick a random starting position
start = random.randint(0, len(encoded_notes) - SEQUENCE_LENGTH - 1)

pattern = encoded_notes[start:start + SEQUENCE_LENGTH]

generated_notes = []

NUM_NOTES = 300

print("\nGenerating Music...\n")

for _ in range(NUM_NOTES):

    input_sequence = np.reshape(pattern, (1, SEQUENCE_LENGTH))

    prediction = model.predict(input_sequence, verbose=0)

    index = np.argmax(prediction)

    result = int_to_note[index]

    generated_notes.append(result)

    pattern.append(index)

    pattern = pattern[1:]

print(f"Generated {len(generated_notes)} notes!")


from pathlib import Path
from midi_utils import create_midi

Path("output").mkdir(exist_ok=True)

create_midi(generated_notes)