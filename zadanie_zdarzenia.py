# =============================================================
# ZADANIE — Analiza zdarzeń lotniczych 2026
# =============================================================

# TODO 1: zaimportuj dane z pliku dane_zdarzenia.py


# TODO 2,3: zaimportuj PrettyTable, SINGLE_BORDER


# =============================================================
# ZMIENNE POMOCNICZE
# =============================================================

# TODO 4: stwórz słownik do zliczania powagi z kluczami "minor" i "serious" = 0

# TODO 5: stwórz pusty słownik do zliczania lotnisk

# TODO 6: stwórz pusty słownik do zliczania samolotów

# TODO 7: stwórz pusty słownik do zliczania typów zdarzeń

# TODO 8: stwórz pustą listę na daty

# =============================================================
# PĘTLA PO DANYCH
# =============================================================

# TODO 9: pętla for po zdarzeniach
# TODO 10: w pętli rozpakuj krotkę: data, lotnisko, typ, powaga, samolot = zdarzenie
# TODO 11: dopisuj datę do listy daty przez .append()
# TODO 12: zliczaj powagę: licznik_powaga[powaga] += 1
# TODO 13: zliczaj lotniska — sprawdź czy klucz istnieje, jeśli nie dodaj z wartoscia = 0, potem += 1
# TODO 14: zliczaj samoloty — tak samo jak lotniska
# TODO 15: zliczaj typy zdarzeń — tak samo jak lotniska


# =============================================================
# OBLICZENIA KOŃCOWE
# =============================================================

# TODO 16: policz łączną liczbę zdarzeń przez len()

# TODO 17: znajdź min i max z listy daty

# TODO 18: znajdź lotnisko_max z największą liczbą zdarzeń lotnisko_max_ile — pętla z if ile > max_ile

# TODO 19: znajdź najczęstszy samolot — tak samo

# TODO 20: znajdź najczęstszy typ zdarzenia — tak samo

# =============================================================
# PRETTYTABLE
# =============================================================

# TODO 21: stwórz tabelę z kolumnami: Lotnisko, Liczba zdarzeń
# TODO 22: pętla po słowniku licznik_lotnisko przez .items() i .add_row()
# TODO 23: ustaw styl SINGLE_BORDER i sortowanie malejące po liczbie: 
# tabela.sortby = "Liczba zdarzeń"
# tabela.reversesort = True


# TODO 24: stwórz tabelę z kolumnami: Typ zdarzenia, Liczba
# TODO 25: pętla po słowniku licznik_typ przez .items() i .add_row()

# TODO 26: stwórz tabelę z kolumnami: Samolot, Liczba zdarzeń
# TODO 27: pętla po słowniku licznik_samolot przez .items() i .add_row()

# =============================================================
# WYŚWIETLANIE
# =============================================================

# TODO 28: wyświetl tabele przez print()
