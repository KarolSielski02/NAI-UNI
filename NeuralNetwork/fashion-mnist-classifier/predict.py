import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np


def predict(image):
    """
    Przewiduje klasę dla danego obrazu za pomocą wytrenowanych modeli.

    Args:
        image (numpy.ndarray): Obraz wejściowy do klasyfikacji.
                               Powinien być tablicą 2D o wymiarach (28, 28).

    Returns:
        int: Przewidziana etykieta klasy dla obrazu wejściowego.
    """
    # Wczytanie wytrenowanych modeli z plików
    small_model = load_model('small_model.keras')
    large_model = load_model('large_model.keras')

    # Przetwarzanie obrazu: zmiana wymiarów na (1, 28, 28, 1) i normalizacja pikseli do zakresu [0, 1]
    image = image.reshape((1, 28, 28, 1)).astype('float32') / 255

    # Przewidywanie klasy za pomocą modeli
    small_model_predictions = small_model.predict(image)
    large_model_predictions = large_model.predict(image)

    # Zwrócenie etykiety klasy z najwyższym prawdopodobieństwem
    return int(np.argmax(small_model_predictions)), int(np.argmax(large_model_predictions))


if __name__ == "__main__":
    """
    Przykład użycia funkcji predict.
    Ładuje zbiór danych Fashion MNIST, wybiera konkretne obrazy testowe i drukuje przewidywane oraz rzeczywiste etykiety.
    """
    # Wczytanie zbioru danych Fashion MNIST
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (_, _), (test_images, test_labels) = fashion_mnist.load_data()

    # Wybór konkretnych obrazów testowych do predykcji
    test_image0 = test_images[0]
    test_image10 = test_images[10]
    test_image100 = test_images[100]

    # Przewidywanie etykiet klas dla wybranych obrazów testowych
    prediction1 = predict(test_image0)
    prediction2 = predict(test_image10)
    prediction3 = predict(test_image100)

    # Wyświetlanie przewidywanych i rzeczywistych etykiet
    print(f'Przewidziana 1. etykieta: mała sieć - {prediction1[0]}, duża sieć - {prediction1[1]}\nRzeczywista etykieta: {test_labels[0]}')
    print(f'Przewidziana 2. etykieta: mała sieć - {prediction2[0]}, duża sieć - {prediction2[1]}\nRzeczywista etykieta: {test_labels[10]}')
    print(f'Przewidziana 3. etykieta: mała sieć - {prediction3[0]}, duża sieć - {prediction3[1]}\nRzeczywista etykieta: {test_labels[100]}')
