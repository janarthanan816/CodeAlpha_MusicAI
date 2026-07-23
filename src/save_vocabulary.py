from load_notes import load_notes
from tokenizer import build_vocabulary
from vocabulary import save_vocabulary

notes = load_notes()

note_to_int, int_to_note = build_vocabulary(notes)

save_vocabulary(note_to_int, int_to_note)