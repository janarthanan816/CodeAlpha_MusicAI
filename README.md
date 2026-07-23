# CodeAlpha_MusicAI

MusicAI is a deep learning project developed during the **CodeAlpha Python Programming Internship**. The objective of this project is to train a neural network on MIDI datasets to learn musical patterns and generate new musical compositions.

## Overview

The project processes MIDI files, extracts notes and chords, converts them into numerical sequences, trains a neural network using TensorFlow/Keras, and generates new music based on the learned patterns.

## Features

* MIDI dataset preprocessing
* Note and chord extraction
* Vocabulary generation and sequence preparation
* Neural network training using TensorFlow/Keras
* Automatic music generation
* MIDI output generation

## Technologies Used

* Python
* TensorFlow
* Keras
* Music21
* NumPy
* Pickle

## Project Structure

```text
CodeAlpha_MusicAI/
├── data/                  # Processed notes and vocabulary
├── dataset/               # MIDI dataset
├── models/                # Trained model
├── output/                # Generated MIDI files
├── src/                   # Source code
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/janarthanan816/CodeAlpha_MusicAI.git
```

Navigate to the project directory:

```bash
cd CodeAlpha_MusicAI
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Train the model:

```bash
python src/train.py
```

Generate music:

```bash
python src/generate.py
```

The generated MIDI file will be stored in the `output` directory.

## Dataset

The model is trained using a collection of classical MIDI compositions from composers including Bach, Beethoven, Mozart, Chopin, and Debussy.

## Learning Outcomes

* Sequence modeling with neural networks
* Music representation using MIDI
* Data preprocessing for deep learning
* Generative AI fundamentals
* TensorFlow model development

## Author

**Janarthanan M**

GitHub: https://github.com/janarthanan816

## Internship

Developed as part of the **CodeAlpha Python Programming Internship**.
