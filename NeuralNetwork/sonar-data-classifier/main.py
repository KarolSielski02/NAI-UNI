import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input


# Załaduj zestaw danych Sonar
url = "sonar.csv"
data = pd.read_csv(url, header=None)

# Sprawdź pierwsze wiersze, aby zrozumieć strukturę danych
print(data.head())

# Przetwarzanie danych
X = data.iloc[:, :-1].values  # Cechy
y = data.iloc[:, -1].values   # Etykiety

# Konwertowanie etykiet kategorycznych ('M' lub 'R') na wartości liczbowe (0 i 1)
y = np.where(y == 'M', 1, 0)

# Normalizacja cech
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Podział danych na zestawy treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Definicja Modelu 1 (Model Sequential)
model1 = Sequential()
model1.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model1.add(Dense(32, activation='relu'))
model1.add(Dense(1, activation='sigmoid'))  # Wyjście klasyfikacji binarnej
model1.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Trenowanie Modelu 1
history1 = model1.fit(X_train, y_train, epochs=50, batch_size=8, validation_split=0.2)

# Ewaluacja Modelu 1 na danych testowych
loss1, accuracy1 = model1.evaluate(X_test, y_test)
print(f"Model 1 Test Loss: {loss1:.4f}, Test Accuracy: {accuracy1*100:.2f}%")

# Definicja Modelu 2 (Alternatywny Model - np. przy użyciu API funkcyjnego Keras)

inputs = Input(shape=(X_train.shape[1],))
x = Dense(64, activation='relu')(inputs)
x = Dense(32, activation='relu')(x)
outputs = Dense(1, activation='sigmoid')(x)
model2 = Model(inputs=inputs, outputs=outputs)
model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Trenowanie Modelu 2
history2 = model2.fit(X_train, y_train, epochs=50, batch_size=8, validation_split=0.2)

# Ewaluacja Modelu 2 na danych testowych
loss2, accuracy2 = model2.evaluate(X_test, y_test)
print(f"Model 2 Test Loss: {loss2:.4f}, Test Accuracy: {accuracy2*100:.2f}%")

# Wizualizacja dokładności treningu i walidacji dla obu modeli
plt.figure(figsize=(12, 6))

# Dokładność Modelu 1
plt.subplot(1, 2, 1)
plt.plot(history1.history['accuracy'], label='Dokładność Treningowa Modelu 1')
plt.plot(history1.history['val_accuracy'], label='Dokładność Walidacyjna Modelu 1')
plt.title('Model 1: Dokładność Treningowa i Walidacyjna')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Dokładność Modelu 2
plt.subplot(1, 2, 2)
plt.plot(history2.history['accuracy'], label='Dokładność Treningowa Modelu 2')
plt.plot(history2.history['val_accuracy'], label='Dokładność Walidacyjna Modelu 2')
plt.title('Model 2: Dokładność Treningowa i Walidacyjna')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()

# Porównanie dokładności testowych obu modeli
print(f"Model 1 Test Accuracy: {accuracy1*100:.2f}%")
print(f"Model 2 Test Accuracy: {accuracy2*100:.2f}%")
