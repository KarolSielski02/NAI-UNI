# Klasyfikacja Danych: Neural Network

Aplikacja służy do klasyfikacji danych za pomocą Sieci Neuronowych oraz wizualizacji danych.

Autorzy: Tomasz Wasielewski (s24280); Karol Sielski (s25)

## Instrukcja uruchomienia

1. **Sklonowanie repozytorium**:
   ```bash
   git clone
   cd NeuralNetwork
   ```

# Utworzenie i aktywacja środowiska wirtualnego: Na systemach Unix (Linux/macOS):
```bash
python3 -m venv .venv
source .venv/bin/activate
```

# Na systemie Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

# Instalowanie zależności
```bash
pip install -r requirements.txt
```

# Uruchomienie aplikacji: 
Aby uruchomić skrypt CIFAR-10:
```bash
cd cifar-10-classifier
python cifar-10.py
```

Aby uruchomić skrypt Sonar:
```bash
cd sonar-data-classifier
python cifar-10.py
```

Aby nauczyć model i uruchomić predykcję - model NN (fshion-mnist):
```bash
cd nashion-mnist-classifier
python train.py
python predict.py
```


Jako 4 przykład z odrębnym zbiorem danych wybraliśmy zbiór danych na temat rozróżniania skóry ludzkiej na obrazie.
Zbiór dostępny jest tutaj: https://archive.ics.uci.edu/dataset/229/skin+segmentation

Aby nauczyć model i uruchomić predykcję - model NN (skin-segmentation):
```bash
cd skin-segmentation-classifier
python train.py
python predict.py
```

# 1. Porównanie wyników klasyfikacji dla różnych algorytmów
Na podstawie przeprowadzonych eksperymentów z danymi Sonar porównano skuteczność trzech algorytmów klasyfikacyjnych: 
drzewa decyzyjnego, SVM oraz sieci neuronowej. 

Poniżej zestawiono kluczowe obserwacje:

1.1 Dokładność:
SVM osiągnęło najwyższą dokładność (85.71%), co wskazuje na jego skuteczność w klasyfikacji sygnałów sonarowych.
Sieć neuronowa uzyskała wynik 83.17%, będąc niewiele gorszą od SVM, co sugeruje potencjał przy odpowiedniej optymalizacji.
Drzewo decyzyjne osiągnęło najniższą dokładność (71.43%), co pokazuje jego ograniczenia w przypadku bardziej złożonych
danych.

1.2 Zrównoważenie wyników dla klas:
SVM lepiej balansuje precyzję i czułość obu klas (skały i miny), co czyni go najbardziej niezawodnym w tej analizie.
Sieć neuronowa była bliska pod względem wyników, lecz jej skuteczność zależy od konfiguracji hiperparametrów.
Drzewo decyzyjne radzi sobie gorzej z identyfikacją obu klas, co wskazuje na problemy z bardziej skomplikowanymi 
granicami decyzyjnymi.

1.3 Wnioski:
SVM okazało się najbardziej efektywne w tym przypadku.
Sieci neuronowe mają potencjał, ale wymagają optymalizacji hiperparametrów i architektury.
Drzewo decyzyjne jest prostsze w implementacji i szybkie w trenowaniu, lecz jego dokładność była najniższa.
Dalsza optymalizacja sieci neuronowej, w tym dostosowanie architektury i procesu uczenia, mogłaby poprawić jej wyniki i 
potencjalnie przewyższyć SVM.


# Wywołanie SVM i DT dla danych sonarowych:
<img width="588" alt="{69673B2E-5639-4AA3-B4D2-B195A7517062}" src="https://github.com/user-attachments/assets/24f253ea-8db2-4b57-8eb9-80e2a130d400" />

# Wywołanie NN dla danych sonarowych:
<img width="889" alt="{DBC03EEC-B2D8-4B00-9BF4-E3D31FA9AAEE}" src="https://github.com/user-attachments/assets/9c7f6520-af40-4a5b-8225-61d75dbd4b32" />
<img width="709" alt="{C23A048B-8DF8-4542-AEA7-6CB1939A83BE}" src="https://github.com/user-attachments/assets/7c4fae3e-cb48-4421-8b7b-c567cace3fc8" />
<img width="729" alt="{3E75D913-60E9-4F22-B444-B803D83E146F}" src="https://github.com/user-attachments/assets/315912c5-81a8-4b33-bd5a-8de6ae03ab4c" />

# Uczenie modelu małej i dużej sieci:
<img width="728" alt="{AE09C9D8-2D5B-43C4-A084-6DF3C7F20C24}" src="https://github.com/user-attachments/assets/7a7f5cdc-b1df-454b-9795-5daff15803fa" />

<img width="747" alt="{49A1AE2D-BCC8-4CD9-BEB6-D792C364645D}" src="https://github.com/user-attachments/assets/3052a7dc-642b-41b5-ad94-13e8ab9c2acf" />


# Wyniki predykcji dla modelu małej i dużej sieci:
<img width="727" alt="{BCE43DF8-142C-49D0-9CDC-D5DA0FB71981}" src="https://github.com/user-attachments/assets/64638df1-22ff-4e2a-92ab-1b5152b86678" />

<img alt="{FDCFFB0A-ABCB-4824-A28B-B5DCC502040D}" src="https://github.com/user-attachments/assets/36c35cd8-1c32-4c76-8d66-f7fe9ff1edc8" />

Rozmiar i głębokość sieci nie mają znaczącego wpływu na wynik przy tak małej skali klasyfikacji i różnorodności dancyh.

# Confussion matrix
![img_6.png](img_6.png)


![img.png](img.png)
