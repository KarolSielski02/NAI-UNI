# Klasyfikator danych

Aplikacja służy do klasyfikacji danych przy użyciu dwóch różnych algorytmów: drzewa decyzyjnego i maszyny wektorów nośnych (SVM). Aplikacja wykonuje następujące kroki:

1. **Ładowanie danych**:
   - Dane Sonar: Zbiór danych zawierający informacje o sygnałach sonarowych, które są klasyfikowane jako odbite od skały (klasa 0) lub od miny (klasa 1).
   - Dane dotyczące przewidywania niewydolności serca: Zbiór danych zawierający informacje o pacjentach, które są klasyfikowane jako mające lub niemające niewydolności serca.

2. **Trenowanie modeli**:
   - Model drzewa decyzyjnego: Algorytm drzewa decyzyjnego jest trenowany na danych treningowych.
   - Model SVM: Algorytm SVM jest trenowany na danych treningowych.

3. **Ocena modeli**:
   - Modele są oceniane na danych testowych przy użyciu metryk takich jak precyzja, czułość, f1-score i dokładność.
   - Wyniki są wyświetlane w formie raportów klasyfikacji.

4. **Wizualizacja danych**:
   - Dane są wizualizowane za pomocą wykresów korelacji (dla danych Sonar) i wykresów punktowych (dla danych dotyczących przewidywania niewydolności serca).

5. **Predykcja dla przykładowych danych**:
   - Modele są używane do przewidywania klasy dla przykładowych danych wejściowych.
     
# Uruchomienie aplikacji

```bash
git clone https://github.com/KarolSielski02/NAI-UNI.git
cd ClassificatorDTSVM
pip install -r requirements.txt
python main.py
```

<img width="363" alt="{5FAD8D75-0660-43A1-BDDB-FD470CEE9BA6}" src="https://github.com/user-attachments/assets/329cf8a5-60c9-45d0-95b9-95c7965c5da1">
<img width="732" alt="{D2F32BD8-5A20-4935-B324-31F73B7DC5A6}" src="https://github.com/user-attachments/assets/2a0f6d9e-d73d-4f71-91a6-d61836f9789b">

<img width="412" alt="{BC4EC28B-53A7-4254-85FC-833CB6BCB9CA}" src="https://github.com/user-attachments/assets/9ac839f6-81a2-4872-abd5-66393cd58dcf">
<img width="477" alt="{8B34254B-9F57-44C4-96EB-E39130B1847E}" src="https://github.com/user-attachments/assets/2f35b467-6880-4559-8e84-8b4bf59093c2">
