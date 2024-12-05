Autorzy: Karol Sielski, Tomasz Wasielewski

Silnik rekomendacji filmów.
Program pozwala na dobranie 5 rekomendacji i antyrekomendacji dla danego użytkownika na podstawie
listy użytkowników podobnych do użytkownika docelowego, sprawdza, które filmy ocenione przez tych użytkowników
nie zostały jeszcze obejrzane przez użytkownika docelowego. Na tej podstawie generuje rekomendacje.

Program określa poziom podobieństwa między użytkownikiem docelowym a innymi użytkownikami
na podstawie ich ocen. Używa metryk odległośći euklidesowej lub korelacja Pearsona

# Zostały przygotowane dwa pliki które przedstawiają działanie progranu na dwa sposoby:

**main.py** - Statyczne podanie rekomendacji i anty rekomendacji dla użytkownika "Tomasz Wasielewski"
z calle'm do TMDB. Wynik printowany jest w konsoli.

**app.py** - Prosta lokalna aplikacja webowa w której możemy wprowadzić swojego użytkownika jak i podać własne
propozycje włącznie z jej oceną i na podstawie tych rekomendacji zostaną nam dobrane filmy,
a wyniki zostaną nam wyświetlone na stronie. Nasze rekomendacje zapisze do lokalnego pliku movie_ratings.json . Opisy są zapewnione przez stronę
TMDB. 

Po odpaleniu w konsoli powinien wyświetlić nam się link do strony. Defaultowo jest to http://127.0.0.1:5000


# Integracja z TMDB
Program komunikuje się ze stroną TMDB w celu pozyskania opisów filmów(opis, rating, tytuł). 
Wyszukiwanie filmu w przypadku podania niepełnego tytułu zwróci nam pierwszy wynik z listy.

# Skopiowanie repozytorium

```bash
git clone https://github.com/KarolSielski02/NAI-UNI.git
cd MovieRecommender
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
lub jeśli nie działa
```bash
pip3 install -r requirements.txt
```

# Plik .env i klucz api
W głównym folderze należy utworzyć plik **.env** i umieścić w nim klucz api który wygenerujemy na tej stronie:
https://developer.themoviedb.org/reference/intro/getting-started

Po zarejestrowaniu się i utworzeniu aplikacji dostaniemy możliwość odczytania naszego klucza api, będzie 
on oznaczony jako: API Read Access Token

Plik .env powinien mieć następujący format
```bash
TMDB_TOKEN=[nasz apikey z TMDB]
```

# Uruchomienie programu
W zależności który plik odpalamy **app.py** czy **main.py** podajemy odpowiednią nazwę pliku w komendzie
```bash
python [main.py / app.py]
```
lub jeśli nie działa
```bash
python3 [main.py / app.py]
```
# Przykład 1 - Karol Sielski
![image](https://github.com/user-attachments/assets/cdaa883f-4ce8-4498-a0ea-76e3df624229)
![image](https://github.com/user-attachments/assets/60ff3527-a80f-4d05-a889-ac87bca44a48)

# Przykład 2 - Tomasz Wasielewski
![image](https://github.com/user-attachments/assets/f71bf3d4-744a-40e9-bf19-51177465765f)
![image](https://github.com/user-attachments/assets/63def19b-8b12-4a86-bfef-9815fb54d18b)

# Przykład 3 - Sandra Homel
![image](https://github.com/user-attachments/assets/4086668f-fc5b-468f-a40c-e5a67bfed797)
![image](https://github.com/user-attachments/assets/4d43409d-3e22-4db0-a0a3-fff6f5fe80a4)

# Przykład pliku movie_ratings.json po wykonaniu przykładów
![image](https://github.com/user-attachments/assets/50f7fb30-2317-45fe-ac0c-4f25645ece03)
![image](https://github.com/user-attachments/assets/022f7259-0562-46d3-8484-7befa20126bc)











