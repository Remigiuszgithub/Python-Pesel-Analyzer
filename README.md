# PESEL Analyzer

## Opis
Program na podstawie numeru PESEL wyznacza datę urodzenia, wiek oraz płeć osoby.

## Jak korzystać
1. Uruchom program.
2. Podaj numer PESEL osoby, której dane chcesz sprawdzić.
3. Program wyświetli datę urodzenia, wiek oraz płeć osoby na podstawie podanego numeru PESEL.

## Jak działa
Program pobiera numer PESEL od użytkownika, a następnie analizuje go, aby wyznaczyć:
- Datę urodzenia (rok, miesiąc, dzień)
- Wiek osoby na podstawie bieżącej daty
- Płeć osoby (kobietę lub mężczyznę) na podstawie ostatniej cyfry numeru PESEL

## Zoptymalizowany wiek
Wiek jest obliczany zgodnie z aktualną datą, uwzględniając nawet lata przestępne, dzięki wykorzystaniu modułu `datetime`.

## Wymagania
- Python 3.x

## Autor
Ten program został napisany przez Remigiusz Nowakowski.

