from model import create_model
from utils import plot_images
import numpy as np
import gzip
import matplotlib.pyplot as plt


def load_data():
    def load_local_data(path, num_images):
        with gzip.open(path, 'rb') as f:
            f.read(16)
            buf = f.read(28 * 28 * num_images)
            data = np.frombuffer(buf, dtype=np.uint8).reshape(num_images, 28, 28, 1)
        return data

    def load_local_labels(path, num_labels):
        with gzip.open(path, 'rb') as f:
            f.read(8)
            buf = f.read(num_labels)
            labels = np.frombuffer(buf, dtype=np.uint8)
        return labels

    train_images = load_local_data('data/train-images-idx3-ubyte.gz', 60000)
    train_labels = load_local_labels('data/train-labels-idx1-ubyte.gz', 60000)
    test_images = load_local_data('data/t10k-images-idx3-ubyte.gz', 10000)
    test_labels = load_local_labels('data/t10k-labels-idx1-ubyte.gz', 10000)

    train_images = train_images.astype('float32') / 255
    test_images = test_images.astype('float32') / 255

    return (train_images, train_labels), (test_images, test_labels)


def train_and_compare():
    (train_images, train_labels), (test_images, test_labels) = load_data()

    # Visualize the data
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    plot_images(train_images.squeeze(), train_labels, class_names)

    # Trening małej sieci
    print("Trening małej sieci...")
    small_model = create_model(size='small')
    small_history = small_model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

    # Trening dużej sieci
    print("Trening dużej sieci...")
    large_model = create_model(size='large')
    large_history = large_model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

    # Zapis modeli
    small_model.save('small_model.keras')
    large_model.save('large_model.keras')

    # Wizualizacja porównania dokładności
    plt.figure(figsize=(10, 5))
    plt.plot(small_history.history['val_accuracy'], label='Mała sieć - Val Accuracy')
    plt.plot(large_history.history['val_accuracy'], label='Duża sieć - Val Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Porównanie dokładności walidacji')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    train_and_compare()
