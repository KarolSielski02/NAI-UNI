import matplotlib.pyplot as plt


def plot_accuracy(history):
    """
    Wizualizuje dokładność modelu na przestrzeni epok.

    Argumenty:
        history (tf.keras.callbacks.History): Historia treningu zawierająca dokładność i stratę.
    """
    plt.plot(history.history['accuracy'], label='dokładność')
    plt.plot(history.history['val_accuracy'], label='dokładność walidacyjna')
    plt.xlabel('Epoka')
    plt.ylabel('Dokładność')
    plt.ylim([0, 1])
    plt.legend(loc='lower right')
    plt.show()
