from music21 import stream, note, chord


def create_midi(prediction_output, filename="output/generated_music.mid"):

    output_notes = []

    offset = 0

    for pattern in prediction_output:

        if "." in pattern or pattern.isdigit():

            notes_in_chord = pattern.split(".")

            chord_notes = []

            for current_note in notes_in_chord:

                new_note = note.Note(int(current_note))

                new_note.offset = offset

                chord_notes.append(new_note)

            new_chord = chord.Chord(chord_notes)

            output_notes.append(new_chord)

        else:

            new_note = note.Note(pattern)

            new_note.offset = offset

            output_notes.append(new_note)

        offset += 0.5

    midi_stream = stream.Stream(output_notes)

    midi_stream.write("midi", fp=filename)

    print(f"MIDI saved as {filename}")