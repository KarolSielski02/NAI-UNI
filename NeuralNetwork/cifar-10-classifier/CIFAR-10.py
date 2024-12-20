from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

"""
Autorzy: Tomasz Wasielewski, Karol Sielski

Ten skrypt implementuje klasyfikator obrazów oparty na konwolucyjnej sieci neuronowej (CNN) 
dla zbioru danych CIFAR-10. Zawiera proces przygotowania danych, definicji modelu, trenowania, 
ewaluacji oraz wizualizacji wyników.

1. Załadowanie zbioru danych CIFAR-10:
   - CIFAR-10 to zbiór obrazów o wymiarach 32x32 z 10 klasami (np. samoloty, koty, psy, itd.).
   - Dane są podzielone na zbiór treningowy i testowy.

2. Przygotowanie danych:
   - Dane wejściowe (obrazy) są normalizowane do zakresu [0, 1], aby poprawić szybkość i stabilność trenowania.
   - Etykiety (klasy) są konwertowane na format one-hot encoding.

3. Definicja modelu CNN:
   - Model zawiera warstwy konwolucyjne (Conv2D), warstwy maksymalnego pooling’u (MaxPooling2D), 
     warstwę spłaszczającą (Flatten) oraz warstwy gęste (Dense).
   - Ostatnia warstwa posiada 10 neuronów z funkcją aktywacji softmax, ponieważ problem dotyczy klasyfikacji 10 klas.

4. Kompilacja modelu:
   - Optymalizator: Adam
   - Funkcja kosztu: categorical_crossentropy (dla problemu wieloklasowej klasyfikacji)
   - Metryka: dokładność (accuracy)

5. Trenowanie modelu:
   - Model jest trenowany przez 10 epok z użyciem wsadu (batch) o rozmiarze 64.
   - Dane walidacyjne są używane do monitorowania jakości modelu.

6. Ewaluacja modelu:
   - Model jest oceniany na zbiorze testowym pod kątem straty (loss) oraz dokładności (accuracy).

7. Wizualizacja wyników:
   - Wykres dokładności treningowej i walidacyjnej w czasie epok.
   - Wykres strat treningowych i walidacyjnych w czasie epok.

Wyniki:
- Wydruk straty testowej oraz dokładności modelu.
- Wykresy pozwalające analizować proces trenowania i jakość modelu.
"""

# Załaduj dane
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalizacja danych
x_train, x_test = x_train / 255.0, x_test / 255.0

# Przekształć etykiety na kategorie
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Definicja modelu CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')  # 10 klas (np. psy, koty, itd.)
])

# Kompilacja modelu
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Trenowanie modelu
history = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))

# Ewaluacja modelu
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy*100:.2f}%")

# Wizualizacja wyników
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()
