import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

# Load Sonar dataset (replace with your actual file path or URL)
url = "sonar.csv"
data = pd.read_csv(url, header=None)

# Check the first few rows to understand the structure
print(data.head())

# Preprocessing
X = data.iloc[:, :-1].values  # Features
y = data.iloc[:, -1].values   # Labels

# Convert categorical labels ('M' or 'R') to numeric values (0 and 1)
y = np.where(y == 'M', 1, 0)

# Normalize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define Model 1 (Sequential Model)
model1 = Sequential()
model1.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model1.add(Dense(32, activation='relu'))
model1.add(Dense(1, activation='sigmoid'))  # Binary classification output
model1.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train Model 1
history1 = model1.fit(X_train, y_train, epochs=50, batch_size=8, validation_split=0.2)

# Evaluate Model 1 on the test data
loss1, accuracy1 = model1.evaluate(X_test, y_test)
print(f"Model 1 Test Loss: {loss1:.4f}, Test Accuracy: {accuracy1*100:.2f}%")

# Define Model 2 (Alternative Model - e.g., using Keras functional API)
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input

inputs = Input(shape=(X_train.shape[1],))
x = Dense(64, activation='relu')(inputs)
x = Dense(32, activation='relu')(x)
outputs = Dense(1, activation='sigmoid')(x)
model2 = Model(inputs=inputs, outputs=outputs)
model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train Model 2
history2 = model2.fit(X_train, y_train, epochs=50, batch_size=8, validation_split=0.2)

# Evaluate Model 2 on the test data
loss2, accuracy2 = model2.evaluate(X_test, y_test)
print(f"Model 2 Test Loss: {loss2:.4f}, Test Accuracy: {accuracy2*100:.2f}%")

# Plot training and validation accuracy for both models
plt.figure(figsize=(12, 6))

# Model 1 Accuracy
plt.subplot(1, 2, 1)
plt.plot(history1.history['accuracy'], label='Model 1 Training Accuracy')
plt.plot(history1.history['val_accuracy'], label='Model 1 Validation Accuracy')
plt.title('Model 1: Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Model 2 Accuracy
plt.subplot(1, 2, 2)
plt.plot(history2.history['accuracy'], label='Model 2 Training Accuracy')
plt.plot(history2.history['val_accuracy'], label='Model 2 Validation Accuracy')
plt.title('Model 2: Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()

# Compare test accuracies
print(f"Model 1 Test Accuracy: {accuracy1*100:.2f}%")
print(f"Model 2 Test Accuracy: {accuracy2*100:.2f}%")