import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

"""
Flag Recognition Model Training

Authors: Tomasz Wasielewski, Karol Wasielewski

This script trains a convolutional neural network (CNN) to recognize flags of three different countries: Polish, Russian, and Ukrainian. The model is trained using images stored in a directory and is saved as a .keras file for later use.

Steps:
1. Define image dimensions and batch size.
2. Create an ImageDataGenerator for loading and augmenting images.
3. Define the CNN model architecture.
4. Compile the model.
5. Train the model using the training and validation data.
6. Save the trained model.

Arguments and their values:
- img_height, img_width: The dimensions to which all images are resized. A common size for CNNs is 224x224 pixels.
- batch_size: The number of images processed in each training step. A batch size of 16 is chosen to balance memory usage and training speed.
- rescale: Rescales the pixel values from [0, 255] to [0, 1] for normalization.
- validation_split: Splits the dataset into training (80%) and validation (20%) sets.
- rotation_range, width_shift_range, height_shift_range, shear_range, zoom_range, horizontal_flip, fill_mode: Data augmentation parameters to improve model generalization by creating variations of the training images.
- optimizer: Adam optimizer is chosen for its efficiency and adaptive learning rate.
- loss: Categorical crossentropy is used as the loss function for multi-class classification.
- metrics: Accuracy is used to evaluate the model's performance.

"""

# Define image dimensions and batch size
img_height, img_width = 224, 224
batch_size = 16

# Create an ImageDataGenerator for loading and augmenting images
train_datagen = ImageDataGenerator(
    rescale=1./255,  # Normalize pixel values to [0, 1]
    validation_split=0.2,  # 20% of the data will be used for validation
    rotation_range=20,  # Randomly rotate images by up to 20 degrees
    width_shift_range=0.2,  # Randomly shift images horizontally by up to 20%
    height_shift_range=0.2,  # Randomly shift images vertically by up to 20%
    shear_range=0.2,  # Randomly apply shearing transformations
    zoom_range=0.2,  # Randomly zoom in on images
    horizontal_flip=True,  # Randomly flip images horizontally
    fill_mode='nearest'  # Fill in missing pixels after transformations
)

train_generator = train_datagen.flow_from_directory(
    'dataset/',  # Directory containing the training images
    target_size=(img_height, img_width),  # Resize images to 224x224 pixels
    batch_size=batch_size,  # Process 16 images at a time
    class_mode='categorical',  # Multi-class classification
    subset='training'  # Use this subset for training
)

validation_generator = train_datagen.flow_from_directory(
    'dataset/',  # Directory containing the validation images
    target_size=(img_height, img_width),  # Resize images to 224x224 pixels
    batch_size=batch_size,  # Process 16 images at a time
    class_mode='categorical',  # Multi-class classification
    subset='validation'  # Use this subset for validation
)

# Define your model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),  # First convolutional layer
    MaxPooling2D((2, 2)),  # First max pooling layer
    Dropout(0.25),  # Dropout to prevent overfitting
    Conv2D(64, (3, 3), activation='relu'),  # Second convolutional layer
    MaxPooling2D((2, 2)),  # Second max pooling layer
    Dropout(0.25),  # Dropout to prevent overfitting
    Conv2D(128, (3, 3), activation='relu'),  # Third convolutional layer
    MaxPooling2D((2, 2)),  # Third max pooling layer
    Flatten(),  # Flatten the output for the fully connected layers
    Dense(128, activation='relu'),  # Fully connected layer with 128 units
    Dropout(0.5),  # Dropout to prevent overfitting
    Dense(3, activation='softmax')  # Output layer with 3 units for 3 classes
])

# Compile the model
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    epochs=10,  # Train for 10 epochs
    validation_data=validation_generator  # Use validation data for evaluation
)

# Save the model
model.save('flag_recognition_model.keras')