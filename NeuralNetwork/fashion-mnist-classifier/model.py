from tensorflow.keras import layers, models


def create_model(size='small'):
    """
    Tworzy i zwraca model sieci neuronowej na potrzeby klasyfikacji obrazów Fashion MNIST.

    Args:
        size (str, opcjonalny): Określa rozmiar modelu. Możliwe wartości:
            - 'small': Model prosty, składający się z 1 warstwy konwolucyjnej i 1 gęstej.
            - 'large': Model złożony, zawierający dodatkowe warstwy konwolucyjne i gęste.
          Domyślnie ustawione na 'small'.

    Returns:
        tensorflow.keras.Model: Skonstruowany model sieci neuronowej.

    Model `small`:
        - Warstwa konwolucyjna (32 filtry, kernel 3x3, aktywacja ReLU)
        - Warstwa MaxPooling (2x2)
        - Spłaszczenie (Flatten)
        - Warstwa gęsta (128 neuronów, aktywacja ReLU)
        - Wyjście (10 neuronów, aktywacja softmax)

    Model `large`:
        - 2 Warstwy konwolucyjne (64 i 128 filtry, kernel 3x3, aktywacja ReLU)
        - Warstwy MaxPooling (2x2 po każdej konwolucji)
        - Dropout (redukcja nadmiernego dopasowania)
        - Spłaszczenie (Flatten)
        - 2 Warstwy gęste (256 i 128 neuronów, aktywacja ReLU)
        - Wyjście (10 neuronów, aktywacja softmax)

    Przykład:
        small_model = create_model(size='small')
        large_model = create_model(size='large')
    """
    model = models.Sequential()

    if size == 'small':
        # Mała sieć neuronowa
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))

    elif size == 'large':
        # Duża sieć neuronowa
        model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Flatten())
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))

    else:
        raise ValueError("Invalid size argument. Use 'small' or 'large'.")

    # Kompilacja modelu
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model
