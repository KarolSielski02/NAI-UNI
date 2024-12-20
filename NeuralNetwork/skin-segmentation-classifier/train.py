from ucimlrepo import fetch_ucirepo
from model import create_model
from utils import plot_accuracy
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


def load_data():
    """
    Wczytuje zbiór danych Skin Segmentation z repozytorium UCI za pomocą pakietu ucimlrepo.

    Zwraca:
        tuple: Zawiera dane treningowe i testowe w formacie:
            (train_features, train_labels), (test_features, test_labels).
    """
    skin_segmentation = fetch_ucirepo(id=229)
    X = skin_segmentation.data.features
    y = skin_segmentation.data.targets - 1  # Zmiana etykiet z 1, 2 na 0, 1

    # Podział danych na zbiór treningowy i testowy
    train_size = int(0.8 * len(X))
    train_features, test_features = X[:train_size], X[train_size:]
    train_labels, test_labels = y[:train_size], y[train_size:]

    return (train_features, train_labels), (test_features, test_labels)

def plot_confusion_matrix(true_labels, predicted_labels):
    """
    Rysuje macierz konfuzji (confusion matrix) przy użyciu funkcji ConfusionMatrixDisplay z pakietu sklearn.

    Argumenty:
        true_labels (array-like): Rzeczywiste (prawdziwe) etykiety klas.
        predicted_labels (array-like): Przewidywane etykiety klas zwrócone przez model.
    """
    cm = confusion_matrix(true_labels, predicted_labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Macierz konfuzji")
    plt.show()

def train():
    """
    Trenuje model na danych do segmentacji skóry, wizualizuje dokładność oraz rysuje macierz konfuzji.
    """
    # Wczytanie danych
    (train_features, train_labels), (test_features, test_labels) = load_data()

    # Tworzenie modelu i trening
    model = create_model()
    history = model.fit(train_features, train_labels, epochs=10, validation_data=(test_features, test_labels))

    # Zapis modelu
    model.save('skin_segmentation_model.keras')

    # Wizualizacja dokładności
    plot_accuracy(history)

    # Przewidywanie na danych testowych
    predicted_labels = model.predict(test_features).argmax(axis=1)

    # Rysowanie macierzy konfuzji
    plot_confusion_matrix(test_labels, predicted_labels)


if __name__ == "__main__":
    train()
