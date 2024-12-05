import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns


"""
Autorzy:
        Tomasz Wasielewski s24280
        Karol Sielski s25944


Aplikacja służy do klasyfikacji danych przy użyciu dwóch różnych algorytmów: 
drzewa decyzyjnego i maszyny wektorów nośnych (SVM). 

Aplikacja wykonuje następujące kroki:

1. Ładowanie danych:

    Dane Sonar: Zbiór danych zawierający informacje o sygnałach sonarowych, 
    które są klasyfikowane jako odbite od skały (klasa 0) lub od miny (klasa 1).
    
    Dane dotyczące przewidywania niewydolności serca: Zbiór danych zawierający 
    informacje o pacjentach, które są klasyfikowane jako posiadający lub nieposiadający niewydolności serca.

2. Trenowanie modeli:

    Model drzewa decyzyjnego: Algorytm drzewa decyzyjnego jest trenowany na danych treningowych.
    Model SVM: Algorytm SVM jest trenowany na danych treningowych.
    
3. Metryki użyte do oceny modeli
    
    Precyzja (Precision):
    Precyzja to stosunek liczby prawdziwie pozytywnych predykcji do sumy liczby prawdziwie pozytywnych i fałszywie 
    pozytywnych predykcji. Wskazuje, jak wiele z przewidywanych pozytywnych przypadków jest rzeczywiście pozytywnych.
    Jest szczególnie ważna, gdy koszt fałszywie pozytywnych wyników jest wysoki.
    
    Czułość (Recall):
    Czułość to stosunek liczby prawdziwie pozytywnych predykcji do sumy liczby prawdziwie pozytywnych i fałszywie 
    negatywnych predykcji. Wskazuje, jak wiele z rzeczywistych pozytywnych przypadków zostało poprawnie 
    zidentyfikowanych przez model. Jest szczególnie ważna, gdy koszt fałszywie negatywnych wyników jest wysoki.
    
    F1-score:
    F1-score to średnia harmoniczna precyzji i czułości.
    Jest używana jako pojedyncza metryka do oceny modelu, gdy chcemy zrównoważyć precyzję i czułość.
    Jest szczególnie przydatna, gdy mamy do czynienia z niezrównoważonymi danymi.
    
    Dokładność (Accuracy):
    Dokładność to stosunek liczby prawdziwie pozytywnych i prawdziwie negatywnych predykcji do całkowitej liczby 
    predykcji. Wskazuje, jak wiele z wszystkich przypadków zostało poprawnie sklasyfikowanych przez model.
    Jest używana jako ogólna miara wydajności modelu, ale może być myląca w przypadku niezrównoważonych danych.
    
    Support:
    Support to liczba prawdziwych wystąpień każdej klasy w danych testowych.
    Jest używana do zrozumienia rozkładu klas w danych testowych.
    
4. Wizualizacja danych:

    Dane są wizualizowane za pomocą wykresów korelacji (dla danych Sonar) i wykresów punktowych (dla danych dotyczących
    przewidywania niewydolności serca).
    
5. Predykcja dla przykładowych danych:

    Modele są używane do przewidywania klasy dla przykładowych danych wejściowych.
    
"""


def load_heart_data():
    """
    Ładuje dane dotyczące przewidywania niewydolności serca.

    Zwraca:
        tuple: Zestawy treningowe i testowe dla cech (X) i etykiet (y).
    """
    data_heart = pd.read_csv("heart.csv")
    X_heart = data_heart.drop('HeartDisease', axis=1)
    y_heart = data_heart['HeartDisease']

    # Zakoduj wartości tekstowe jako wartości numeryczne
    X_heart = pd.get_dummies(X_heart, drop_first=True)

    return train_test_split(X_heart, y_heart, test_size=0.2, random_state=42)


def load_sonar_data():
    """
    Ładuje dane pomiarowe sonaru.

    Zwraca:
        tuple: Zestawy treningowe i testowe dla cech (X) i etykiet (y).
    """
    url_sonar = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar"
                 "/sonar.all-data")
    data_sonar = pd.read_csv(url_sonar, header=None)
    X_sonar = data_sonar.drop(60, axis=1)
    y_sonar = data_sonar[60].apply(lambda x: 1 if x == 'M' else 0)
    return train_test_split(X_sonar, y_sonar, test_size=0.2, random_state=42)


def train_decision_tree(x_train, y_train):
    """
    Trenuje model drzewa decyzyjnego.

    Argumenty:
        x_train (DataFrame): Dane treningowe.
        y_train (Series): Etykiety treningowe.

    Zwraca:
        DecisionTreeClassifier: Wytrenowany model drzewa decyzyjnego.
    """
    tree_clf = DecisionTreeClassifier(random_state=42)
    tree_clf.fit(x_train, y_train)
    return tree_clf


def train_svm(x_train, y_train):
    """
    Trenuje model SVM.

    Argumenty:
        x_train (DataFrame): Dane treningowe.
        y_train (Series): Etykiety treningowe.

    Zwraca:
        SVC: Wytrenowany model SVM.
    """
    svm_clf = SVC(kernel='linear', random_state=42)
    svm_clf.fit(x_train, y_train)
    return svm_clf


def evaluate_model(model, x_test, y_test, model_name):
    """
    Ocena modelu na danych testowych.

    Argumenty:
        model: Wytrenowany model.
        x_test (DataFrame): Dane testowe.
        y_test (Series): Etykiety testowe.
        model_name (str): Nazwa modelu.
    """
    y_predicted = model.predict(x_test)
    print(f"{model_name} - Raport klasyfikacji:")
    print(classification_report(y_test, y_predicted))
    print(f"{model_name} - Dokładność:", accuracy_score(y_test, y_predicted))


def visualize_data_sonar(data):
    """
    Wizualizacja danych Sonar.

    Argumenty:
        data (DataFrame): Dane do wizualizacji.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, fmt=".2f")
    plt.show()


def visualize_data_heart(data):
    """
    Wizualizacja danych Heart Failure Prediction.

    Argumenty:
        data (DataFrame): Dane do wizualizacji.
    """
    sns.scatterplot(x='Age', y='RestingBP', hue='HeartDisease', data=data)
    plt.show()


def predict_sample(model, sample_data, model_name, feature_names):
    """
    Predykcja dla przykładowych danych.

    Argumenty:
        model: Wytrenowany model.
        sample_data (list): Przykładowe dane.
        model_name (str): Nazwa modelu.
        feature_names (list): Nazwy cech.
    """
    sample_df = pd.DataFrame(sample_data, columns=feature_names)
    prediction = model.predict(sample_df)
    print(f"{model_name} - Predykcja dla przykładowych danych:", prediction)


def main():
    """
    Główna funkcja uruchamiająca cały proces klasyfikacji i oceny modeli.
    """
    # Sonar Data
    x_train_sonar, x_test_sonar, y_train_sonar, y_test_sonar = load_sonar_data()
    tree_clf_sonar = train_decision_tree(x_train_sonar, y_train_sonar)
    svm_clf_sonar = train_svm(x_train_sonar, y_train_sonar)
    evaluate_model(tree_clf_sonar, x_test_sonar, y_test_sonar, "Sonar - Drzewo decyzyjne")
    evaluate_model(svm_clf_sonar, x_test_sonar, y_test_sonar, "Sonar - SVM")
    visualize_data_sonar(pd.concat([x_train_sonar, y_train_sonar], axis=1))
    sample_data_sonar = [x_train_sonar.iloc[0].tolist()]
    print(sample_data_sonar)
    predict_sample(tree_clf_sonar, sample_data_sonar, "Sonar - Drzewo decyzyjne", x_train_sonar.columns)
    predict_sample(svm_clf_sonar, sample_data_sonar, "Sonar - SVM", x_train_sonar.columns)

    # Heart Failure Prediction Data
    x_train_heart, x_test_heart, y_train_heart, y_test_heart = load_heart_data()
    tree_clf_heart = train_decision_tree(x_train_heart, y_train_heart)
    svm_clf_heart = train_svm(x_train_heart, y_train_heart)
    evaluate_model(tree_clf_heart, x_test_heart, y_test_heart, "Heart Failure - Drzewo decyzyjne")
    evaluate_model(svm_clf_heart, x_test_heart, y_test_heart, "Heart Failure - SVM")
    visualize_data_heart(pd.concat([x_train_heart, y_train_heart], axis=1))
    sample_data_heart = [x_train_heart.iloc[2].tolist()]
    print(sample_data_heart)
    predict_sample(tree_clf_heart, sample_data_heart, "Heart Failure - Drzewo decyzyjne", x_train_heart.columns)
    predict_sample(svm_clf_heart, sample_data_heart, "Heart Failure - SVM", x_train_heart.columns)


if __name__ == "__main__":
    main()
