from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout


def build_model(vocab_size, sequence_length):

    model = Sequential()

    # Convert note IDs into vectors
    model.add(
        Embedding(
            input_dim=vocab_size,
            output_dim=100
        )
    )

    # Learn musical patterns
    model.add(
        LSTM(
            units=256
        )
    )

    # Prevent overfitting
    model.add(
        Dropout(
            0.3
        )
    )

    # Predict next note
    model.add(
        Dense(
            units=vocab_size,
            activation="softmax"
        )
    )

    return model