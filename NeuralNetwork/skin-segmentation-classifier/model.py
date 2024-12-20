from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer


def create_model():
    """
    Tworzy i kompiluje model sieci neuronowej do klasyfikacji segmentacji skóry.

    Architektura modelu:
    - Warstwa wejściowa: 3 neurony (dla 3 cech: B, G, R)
    - Warstwa ukryta: 128 neuronów, funkcja aktywacji ReLU
    - Warstwa wyjściowa: 2 neurony, funkcja aktywacji softmax (dla 2 klas: skóra, brak skóry)

    Model jest kompilowany z następującymi ustawieniami:
    - Optymalizator: Adam
    - Funkcja straty: Sparse Categorical Crossentropy
    - Metryka: Dokładność (Accuracy)

    Zwraca:
        model (tf.keras.Model): Skompilowany model sieci neuronowej.
    """
    model = Sequential([
        InputLayer(input_shape=(3,)),
        Dense(128, activation='relu'),
        Dense(2, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model
