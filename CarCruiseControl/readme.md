Symulacja logiki fuzzy na przykładzie tempomatu w samochodzie. 
Zaprogramowana logika programu zwraca użytkownikowi decyzję o przyspieszeniu, hamowaniu lub utrzymaniu prędkości w różnym natężeniu,
w zależności od przekazanych warunków pogodowych, obecnej prędkości oraz dystansu od następnego pojazdu.

W pliku main.py znajduje się funkcja uruchamiająca symulację, do której przekazać należy ilość sekund (sos),
by określić czas trwania symulacji.


# Skopiowanie repozytorium

```bash
git clone https://github.com/KarolSielski02/NAI-UNI.git
cd CarCruiseControl
```

# Utworzenie środowiska wirtualnego
Aby uniknąć konfliktów z innymi projektami, najlepiej jest stworzyć środowisko wirtualne.

Utwórz środowisko wirtualne:

Dla systemów Windows:
```bash
python -m venv .venv
```

Dla systemów Linux/macOS:

```bash
python3 -m venv .venv
```

# Aktywuj środowisko wirtualne

Dla systemów Windows:

```bash
.venv\Scripts\activate
```

Dla systemów Linux/macOS:

```bash
source .venv/bin/activate
```

# Instalacja zależności

```bash
pip install -r requirements.txt
```

# Uruchomienie programu

```bash
python main.py
```

# Harsh decelerate 
<img width="442" alt="{5BF44297-E367-4676-BC16-D5DF7AC0BF0C}" src="https://github.com/user-attachments/assets/a990b80f-9f02-4e32-8353-cd50460a00d0">

# Decelerate 
<img width="421" alt="{483EFFB8-4EE2-482E-BBDA-99C1434FCE10}" src="https://github.com/user-attachments/assets/a7e1f4d5-90af-4d3d-b9cc-4559941e1f30">

# Maintain
<img width="410" alt="{5610A227-6F17-4DFA-9BFA-63523A8020F8}" src="https://github.com/user-attachments/assets/11a34f4c-c5cb-4285-9c2b-91e77d96ec5f">

# Accelerate
<img width="407" alt="{7F6FAF34-E6B8-46BF-85FE-8FDC8D942741}" src="https://github.com/user-attachments/assets/e3e8b960-252f-4f4e-925b-1c29748dd5d2">








