# 📌 Symboliczne Różniczkowanie i Upraszczanie Wyrażeń Matematycznych

## 📖 Opis Projektu
Projekt jest biblioteką napisaną w Pythonie, która umożliwia **symboliczne różniczkowanie**, **upraszczanie** oraz **przetwarzanie** wyrażeń matematycznych. Obsługiwane są podstawowe operacje arytmetyczne, funkcje trygonometryczne, logarytmy oraz inne funkcje matematyczne. Projekt jest zaimplementowany w **modularny sposób**, z wykorzystaniem bibliotek **PLY (Python Lex-Yacc)** do analizy składniowej i leksykalnej.

### ✨ Kluczowe Funkcjonalności
- 🧮 **Symboliczne różniczkowanie**: Automatyczne obliczanie pochodnych dla wyrażeń matematycznych.
- 🔄 **Upraszczanie wyrażeń**: Redukcja wyrażeń do prostszych postaci, np. `ln(e)` do `1`.
- 📏 **Obsługa funkcji matematycznych**: Trygonometrycznych (`sin`, `cos`, `tan`), hiperbolicznych (`sinh`, `cosh`, `tanh`), logarytmicznych (`ln`), potęgowych, pierwiastków i innych.
- 🔤 **Obsługa zmiennych i stałych**: Możliwość pracy z dowolnymi zmiennymi oraz predefiniowanymi stałymi (`pi`, `e`).
- 📦 **Modularna budowa**: Lexer, parser i system symboli są rozdzielone w osobnych modułach.

## 📜 Gramatyka w Postaci BNF
```
<expression> ::= <addition_or_subtraction>

<addition_or_subtraction> ::= <multiplication_or_division> "+" <addition_or_subtraction>
                            | <multiplication_or_division> "-" <addition_or_subtraction>
                            | <multiplication_or_division>

<multiplication_or_division> ::= <exponentiation> "*" <multiplication_or_division>
                               | <exponentiation> "/" <multiplication_or_division>
                               | <exponentiation>

<exponentiation> ::= <unary_operation> "^" <exponentiation>
                   | <unary_operation>

<unary_operation> ::= "-" <primary_expression>
                    | <primary_expression>

<primary_expression> ::= <function_call>
                       | <group>
                       | <constant>
                       | <number>
                       | <variable>

<function_call> ::= "sin" "(" <expression> ")"
                  | "cos" "(" <expression> ")"
                  | "ln" "(" <expression> ")"
                  | "sqrt" "(" <expression> ")"
                  | "abs" "(" <expression> ")"
                  | "exp" "(" <expression> ")"
                  | "sinh" "(" <expression> ")"
                  | "cosh" "(" <expression> ")"
                  | "tanh" "(" <expression> ")"
                  | "asin" "(" <expression> ")"
                  | "acos" "(" <expression> ")"
                  | "atan" "(" <expression> ")"
                  | "tan" "(" <expression> ")"
                  | "sec" "(" <expression> ")"
                  | "log" "(" <expression> "," <expression> ")"

<group> ::= "(" <expression> ")"

<constant> ::= "pi"
             | "e"

<number> ::= {0-9}+ ("." {0-9}+)?
<variable> ::= {a-zA-Z_} {a-zA-Z0-9_}*
```

## 📂 Struktura Projektu
```
symbolic_differenation/
├── symbolic/
│   ├── __init__.py       # Plik inicjalizujący pakiet.
│   ├── symbolic_math.py  # Klasy reprezentujące symbole matematyczne.
│   ├── lexer.py          # Lexer: analiza leksykalna (tokenizacja).
│   ├── parser.py         # Parser: analiza składniowa wyrażeń.
├── main.py               # Podstawowy plik demonstracyjny.
├── main_gui.py           # Plik demonstracyjny z interfejsem graficznym.
└── requirements.txt      # Lista zależności.
```

## 🔧 Instalacja
Wymagania:
- 🐍 Python 3.8+
- 📦 Biblioteka `ply`

### 🛠 Instalacja zależności
```sh
pip install -r requirements.txt
```

## 🚀 Jak uruchomić
1. Upewnij się, że wszystkie pliki są w odpowiednich lokalizacjach.
2. Uruchom `main.py`, aby przetestować różne wyrażenia matematyczne:

```sh
python main.py
```

📌 Przykładowy wynik:
```
Wyrażenie: ln(x^2)
Parsowane wyrażenie: ln((x^2))
Pochodna: ((2 * x) * ((x^2)^-1))
```

## 🎯 Przykłady Użycia

### ✏️ Tworzenie wyrażeń
```python
from symbolic.parser import parser

expr = "x^2 + 3*x + 5"
expr = parser.parse(expr_str)
print(expr)  # ((x^2) + (3 * x)) + 5)
```

### 🔢 Różniczkowanie
```python
derivative = expr.differentiate("x")
print(derivative)  # (((((2 * (x^(2 + -1))) * 1) + (((x^2) * ln(x)) * 0)) + ((0 * x) + (3 * 1))) + 0)
```

### 🔄 Upraszczanie
```python
simplified = derivative.simplify()
print(simplified)  # ((2 * x) + 3)
```

## 🏗 Obsługiwane Funkcje Matematyczne
- **Podstawowe operatory**: `+`, `-`, `*`, `/`, `^` (potęgowanie).
- **Funkcje trygonometryczne**: `sin`, `cos`, `tan`, `sec`.
- **Funkcje odwrotne funkcji trygonmetrycznych**: `asin`, `acos`, `atan`.
- **Funkcje hiperboliczne**: `sinh`, `cosh`, `tanh`.
- **Logarytmy**: `ln` (logarytm naturalny), `log` (logarytm o zmiennej podstawie).
- **Inne**: `sqrt` (pierwiastek), `abs` (wartość bezwzględna), `exp` (funkcja wykładnicza).

## 📌 Licencja
Projekt jest dostępny na licencji **MIT** ✅

