from save_notes import save_notes
from pathlib import Path
from music21 import converter, note, chord

# Dataset folder
DATASET_PATH = Path("dataset")

# Store every extracted note/chord
all_notes = []

# Find every MIDI file
midi_files = []

for file in DATASET_PATH.rglob("*"):
    if file.is_file() and file.suffix.lower() == ".mid":
        midi_files.append(file)
print(f"Found {len(midi_files)} MIDI files.\n")

# Read each MIDI file
for index, midi_file in enumerate(midi_files, start=1):

    print(f"[{index}/{len(midi_files)}] Reading: {midi_file.name}")

    try:
        midi = converter.parse(midi_file)

        # Read notes and chords
        for element in midi.flatten().notes:

            if isinstance(element, note.Note):
                all_notes.append(str(element.pitch))

            elif isinstance(element, chord.Chord):
                all_notes.append(".".join(str(n) for n in element.normalOrder))

    except Exception as e:
        print(f"Error reading {midi_file.name}: {e}")

print("\n" + "=" * 50)
print(f"Total extracted notes/chords: {len(all_notes)}")
print("=" * 50)

save_notes(all_notes)

print("\nFirst 20 extracted elements:")

for item in all_notes[:20]:
    print(item)