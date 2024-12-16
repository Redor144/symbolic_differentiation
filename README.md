# Symboliczne Różniczkowanie i Upraszczanie Wyrażeń Matematycznych

## Opis Projektu
Ten projekt jest biblioteką napisaną w Pythonie, która umożliwia symboliczne różniczkowanie, upraszczanie oraz przetwarzanie wyrażeń matematycznych. Obsługiwane są podstawowe operacje arytmetyczne, funkcje trygonometryczne, logarytmy oraz inne funkcje matematyczne. Projekt jest zaimplementowany w modularny sposób, z wykorzystaniem bibliotek PLY (Python Lex-Yacc) do analizy składniowej i leksykalnej.

### Kluczowe Funkcjonalności
- **Symboliczne różniczkowanie**: Automatyczne obliczanie pochodnych dla wyrażeń matematycznych.
- **Upraszczanie wyrażeń**: Redukcja wyrażeń do prostszych postaci, np. `ln(e)` do `1`.
- **Obsługa funkcji matematycznych**: Trygonometrycznych (sin, cos, tan), hiperbolicznych (sinh, cosh, tanh), logarytmicznych (ln), potęgowych, pierwiastków, i innych.
- **Obsługa zmiennych i stałych**: Możliwość pracy z dowolnymi zmiennymi oraz predefiniowanymi stałymi (`pi`, `e`).
- **Modularna budowa**: Lexer, parser i system symboli są rozdzielone w osobnych modułach.

## Struktura Projektu

```
symbolic_differenation/
├── symbolic/
│   ├── __init__.py              # Plik inicjalizujący pakiet.
│   ├── symbolic_math.py   # Klasy reprezentujące symbole matematyczne.
│   ├── lexer.py                    # Lexer: analiza leksykalna (tokenizacja).
│   ├── parser.py                  # Parser: analiza składniowa wyrażeń.
├── main.py                         # Główny plik demonstracyjny.
└── requirements.txt            # Lista zależności.
```

### Pliki
- **`symbols.py`**: Definicje klas matematycznych, takich jak `Symbol`, `Variable`, `Constant`, `Add`, `Mul`, `Ln`, itp.
- **`lexer.py`**: Definicja tokenów i analizatora leksykalnego.
- **`parser.py`**: Parser, który generuje wewnętrzną reprezentację wyrażeń.
- **`main.py`**: Przykładowe użycie biblioteki.

## Wymagania
- Python 3.8+
- Biblioteka `ply`

### Instalacja zależności
Użyj poniższego polecenia, aby zainstalować wymagane biblioteki:

```
pip install -r requirements.txt
```

## Jak uruchomić
1. Upewnij się, że wszystkie pliki są w odpowiednich lokalizacjach.
2. Uruchom `main.py`, aby przetestować różne wyrażenia matematyczne:

```
python main.py
```

Przykładowy wynik:
```
Wyrażenie: ln(x^2)
Parsowane wyrażenie: ln((x^2))
Pochodna: ((2 * x) * ((x^2)^-1))
```

## Przykłady Użycia

### Tworzenie wyrażeń
```python
from symbolic.parser import parser

expr = "x^2 + 3*x + 5"
expr = parser.parse(expr_str)
print(expr)  # ((x^2) + (3 * x)) + 5)
```

### Różniczkowanie
```python
derivative = expr.differentiate("x")
print(derivative)  # (((((2 * (x^(2 + -1))) * 1) + (((x^2) * ln(x)) * 0)) + ((0 * x) + (3 * 1))) + 0)
```

### Upraszczanie
```python
simplified = derivative.simplify()
print(simplified)  # ((2 * x) + 3)
```

## Obsługiwane Funkcje Matematyczne
- **Podstawowe operatory**: `+`, `-`, `*`, `/`, `^` (potęgowanie).
- **Funkcje trygonometryczne**: `sin`, `cos`, `tan`, `sec`.
- **Funkcje odwrotne funkcji trygonmetrycznych**: `asin`, `acos`, `atan`.
- **Funkcje hiperboliczne**: `sinh`, `cosh`, `tanh`.
- **Logarytmy**: `ln` (logarytm naturalny), `log` (logarytm o zmiennej podstawie).
- **Inne**: `sqrt` (pierwiastek), `abs` (wartość bezwzględna), `exp` (funkcja wykładnicza).

## Rozwój i Ulepszenia
### Możliwe rozszerzenia:
- Dodanie obsługi większej liczby funkcji matematycznych.
- Obsługa przedziałów i operacji na funkcjach wielowymiarowych.
- Integracja z narzędziami wizualizacyjnymi do rysowania wykresów.

## Licencja
Projekt jest dostępny na licencji MIT
