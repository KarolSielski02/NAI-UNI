from ucimlrepo import fetch_ucirepo
from tensorflow.keras.models import load_model
import numpy as np


def predict(features):
    """
    Przewiduje klasę na podstawie podanych cech przy użyciu wytrenowanego modelu.

    Argumenty:
        features (numpy.ndarray): Wejściowe cechy do klasyfikacji. Powinna to być 1-wymiarowa tablica o kształcie (3,).

    Zwraca:
        int: Przewidywana etykieta klasy dla podanych cech.
    """
    model = load_model('skin_segmentation_model.keras')
    features = features.reshape((1, 3)).astype('float32')
    predictions = model.predict(features)
    return np.argmax(predictions)


if __name__ == "__main__":
    """
    Przykład użycia funkcji predict.
    Ładuje zbiór danych segmentacji skóry, wybiera konkretne próbki testowe i wypisuje przewidywane oraz rzeczywiste etykiety.
    """
    skin_segmentation = fetch_ucirepo(id=229)
    X = skin_segmentation.data.features
    y = skin_segmentation.data.targets - 1  # Etykiety są 1 i 2, zmienia się je na 0 i 1

    # Wybieranie konkretnych próbek testowych do przewidywania
    test_feature0 = X.iloc[0].values
    test_feature10 = X.iloc[10].values
    test_feature100 = X.iloc[100].values

    # Przewidywanie etykiet klas dla wybranych próbek testowych
    prediction1 = predict(test_feature0)
    prediction2 = predict(test_feature10)
    prediction3 = predict(test_feature100)

    # Wypisanie przewidywanych i rzeczywistych etykiet
    print(f'Przewidywana etykieta 1: {prediction1}\nRzeczywista etykieta: {y.iloc[0].item()}')
    print(f'Przewidywana etykieta 2: {prediction2}\nRzeczywista etykieta: {y.iloc[100].item()}')
    print(f'Przewidywana etykieta 3: {prediction3}\nRzeczywista etykieta: {y.iloc[1000].item()}')
