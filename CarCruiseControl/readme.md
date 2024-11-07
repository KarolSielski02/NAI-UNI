# Skopiowanie repozytorium
Sklonuj repozytorium na swoje lokalne urządzenie. W terminalu użyj poniższej komendy:

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
