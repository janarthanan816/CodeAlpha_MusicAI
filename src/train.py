from vocabulary import save_vocabulary
from sklearn.model_selection import train_test_split
from config import SEQUENCE_LENGTH

from load_notes import load_notes
from tokenizer import build_vocabulary, encode_notes
from data_loader import prepare_training_data
from model import build_model


print("=" * 50)
print("Loading Notes...")
print("=" * 50)

notes = load_notes()


print("\nBuilding Vocabulary...")

note_to_int, int_to_note = build_vocabulary(notes)



vocab_size = len(note_to_int)

print(f"Vocabulary Size : {vocab_size}")



print("\nEncoding Notes...")

encoded_notes = encode_notes(notes, note_to_int)

print(f"Encoded Notes : {len(encoded_notes)}")



print("\nPreparing Training Data...")

X, y = prepare_training_data(
    encoded_notes,
    SEQUENCE_LENGTH
)

print(f"X Shape : {X.shape}")
print(f"y Shape : {y.shape}")


print("\nSplitting Dataset...")

X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

print(f"Training Samples : {len(X_train)}")
print(f"Validation Samples : {len(X_val)}")


print("\nBuilding Model...")

model = build_model(
    vocab_size,
    SEQUENCE_LENGTH
)


model.build(input_shape=(None, SEQUENCE_LENGTH))


model.summary()


print("\nCompiling Model...")

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("Model Compiled Successfully!")


print("\nStarting Training...")

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=10,
    batch_size=64
)


from pathlib import Path

Path("models").mkdir(exist_ok=True)

model.save("models/music_generator.keras")

print("\nModel saved successfully!")