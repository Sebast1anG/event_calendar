# Event calendar

Projekt jest odpowiedzią na potrzebę UWS, którą jest kalendarz wydarzeń . Projekt ten ma na celu ułatwienie użytkownikom znalezienia informacji oraz poznanie szczegółów wydarzeń.

## Wymagania

Aby uruchomić ten projekt, potrzebne są następujące narzędzia:

- Python 3.13.0 lub nowszy
- Virtualenv

### Instalacja

1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/Sebast1anG/event_calendar.git
    cd event_calendar
    ```

2. Utwórz i aktywuj środowisko wirtualne:

    - **Na macOS/Linux**:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

    - **Na Windows**:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. Zainstaluj wymagane pakiety:
    ```bash
    pip install -r requirements.txt
    ```

### Konfiguracja

1. Utwórz plik `.env` w katalogu głównym projektu, który zawiera zmienne środowiskowe:
    ```bash
    touch .env
    ```

2. W pliku `.env` dodaj klucz API oraz inne potrzebne ustawienia:
    ```env
    EVENT_API_KEY=Twój_klucz_API
    ```

### Migracje bazy danych

Aby uruchomić migracje i zaktualizować bazę danych, wykonaj następujące polecenia:

```bash
python manage.py makemigrations
python manage.py migrate

### Uruchomienie aplikacji
```bash
 python manage.py runserver
