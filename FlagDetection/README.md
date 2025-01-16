# Flag Recognition Project

This project is designed to recognize flags of three different countries: Polish, Russian, and Ukrainian. It uses a 
convolutional neural network (CNN) to classify images of flags. The project includes scripts for training the model and 
for real-time flag recognition using a webcam.

## Installation

1. **Clone the repository**:
```shell
git clone https://github.com/yourusername/flag-recognition.git
cd flag-recognition
```
   
## Create a virtual environment:
    
```shell
python -m venv venv
```

### Activate the virtual environment:

On Windows:
```shell
venv\Scripts\activate
```
On macOS/Linux:
```shell
source venv/bin/activate
```

## Install the required dependencies:
```shell
pip install -r requirements.txt
```

### Model Training
Prepare your dataset:

Place your training images in a directory named dataset/.
The directory should have subdirectories for each class (e.g., Polish, Russian, Ukrainian).

Run the model training script:
```shell
python train_model.py
```

This script will train the CNN model using the images in the dataset/ directory and save the trained model as flag_recognition_model.keras.

### Flag Prediction
Run the flag prediction script:
```shell
python predict_flags.py
```
This script will capture video from your webcam, detect flags in the video frames, and display the predicted flag labels in real-time.

Authors
Tomasz Wasielewski, Karol Sielski
![ezgif-7-b1b7dbc610.gif](ezgif-7-b1b7dbc610.gif)