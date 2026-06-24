# =============================================================
# ZADANIE — Prognoza pogody vs Pomiary rzeczywiste 2026
# =============================================================

# TODO 1: zaimportuj prognoza i pomiary z pliku dane_prognoza.py
from tkinter import simpledialog
from tkinter import messagebox as mb
from prettytable import PrettyTable as pt
from prettytable import SINGLE_BORDER
from dane_prognoza import prognoza, pomiary

# TODO 2: zaimportuj PrettyTable, SINGLE_BORDER


# TODO 3: zaimportuj messagebox


# =============================================================
# ZMIENNE POMOCNICZE
# =============================================================

# TODO 4: stwórz słownik do zliczania ocen prognozy dobra=0 etc.
licznik_ocen={"dobra":0,"akceptowalna":0,"zla":0}
# TODO 5: stwórz pusty słownik do liczenia "dobre" prognozy per lotnisko
licznik_dobre={}
# =============================================================
# PRETTYTABLE
# =============================================================

# TODO 6: stwórz tabelę z kolumnami:
# Data | Lotnisko | Temp.prog | Temp.rzecz | Odch.temp | Ciśn.prog | Ciśn.rzecz | Odch.ciśn | Wilg.prog | Wilg.rzecz | Odch.wilg | Ocena

tbl=pt()
tbl.set_style(SINGLE_BORDER)
tbl.field_names=['Data' , 'Lotnisko' , 'Temp.prog' , 'Temp.rzecz' , 'Odch.temp' , 'Ciśn.prog' , 'Ciśn.rzecz' , 'Odch.ciśn' , 'Wilg.prog' , 'Wilg.rzecz' , 'Odch.wilg' , 'Ocena']

# =============================================================
# PĘTLA PO DANYCH
# =============================================================

# TODO 7: pętla z zip() łącząca prognozę i pomiary
# for prog, pomiar in zip(prognoza, pomiary):

for prog, pomiar in zip(pomiary,prognoza):
    data_p,lotnisko_p,temp_C_p,cisnienie_hPa_p,wilgotnosc_p=prog
    _,_,temp_C_r,cisnienie_hPa_r,wilgotnosc_r=pomiar


# TODO 8: rozpakuj krotkę prog: data, lotnisko, temp_p, cisn_p, wilg_p = prog
# TODO 9: rozpakuj krotkę pomiar lub pobierz wartości z pomiaru przez indeks

# TODO 10: oblicz odchylenia, zaokrąglij do 1 miejsca, oblicz wartość bezwzględną różnicy - abs()

    o_temp=abs(round(temp_C_p-temp_C_r,1))
    o_cisn=abs(round(cisnienie_hPa_p-cisnienie_hPa_r,1))
    o_wilg=abs(round(wilgotnosc_p-wilgotnosc_r,1))


    # TODO 11: oceń prognozę blokiem if/elif/else wg progów ze slajdu

    if o_temp <= 1 and o_cisn <=2 and o_wilg<=5:
        ocena="dobra"
    elif o_temp <= 3 and o_cisn <=5 and o_wilg<=10:
        ocena="akceptowalna"
    else:
        ocena="zla"

    # TODO 12: zlicz oceny w słowniku licznik_ocen -  +=1

    licznik_ocen[ocena]+=1

    # TODO 13: zlicz "dobre" prognozy per lotnisko w słowniku licznik_dobra
    # jeśli lotnisko nie istnieje w słowniku — dodaj z wartoscią = 0
    # jeśli ocena == "dobra" — dodaj += 1

    if lotnisko_p not in licznik_dobre:
        licznik_dobre[lotnisko_p]=0
    if ocena=="dobra":
        licznik_dobre[lotnisko_p]+=1

# TODO 14: dodaj wiersz do tabeli przez .add_row()
# Data | Lotnisko | Temp.prog | Temp.rzecz | Odch.temp | Ciśn.prog | Ciśn.rzecz | Odch.ciśn | Wilg.prog | Wilg.rzecz | Odch.wilg | Ocena
    tbl.add_row([data_p,lotnisko_p,temp_C_p,temp_C_r,o_temp,cisnienie_hPa_p,cisnienie_hPa_r,o_cisn,wilgotnosc_p,wilgotnosc_r,o_wilg,ocena])


# =============================================================
# OBLICZENIA KOŃCOWE — najlepsza i najgorsza prognoza
# =============================================================

# TODO 15: znajdź najlepsze i najgorsze lotnisko
# pętla po licznik_dobra.items()
# szukaj max i min z if —  
# ile > max_ile         -> max_dobrych = ile, lotnisko_najlepsze = lotnisko  
# lub ile < min_dobrych -> podobnie

lotnisko_najlepsze=""
lotnisko_najgorsze=""
max_dobrych=-1      #conajmniej mniej o 1 niz najmniejszy stan oceny
min_dobrych=600     #wiecej niz 1 patrzac na zawartosc slownika

for lotnisko, ile in licznik_dobre.items():
    if ile > max_dobrych:
        max_dobrych=ile
        lotnisko_najlepsze=lotnisko
    if ile < min_dobrych:
        min_dobrych=ile
        lotnisko_najgorsze=lotnisko
# =============================================================
# WYŚWIETLANIE
# =============================================================

# TODO 16: wyświetl tabelę przez print()
print(tbl)

# TODO 17: zbuduj komunikat z podsumowaniem:
# - ile prognoz dobra / akceptowalna / zła
# - najlepsze i najgorsze lotnisko
# wyświetl przez mb.showinfo()
 #nie powielac znakow jedno wewnatrz drugiego "/'
komentarz=f"PROGNOZY:\n" \
          f"==============================\n" \
          f"Dobra:{licznik_ocen['dobra']}\n" \
          f"Akceptowalna:{licznik_ocen['akceptowalna']}\n" \
          f"Zla:{licznik_ocen['zla']}\n" \
          f"==============================\n" \
          f"Najwiecej dobrych ma lotnisko:{lotnisko_najlepsze}={max_dobrych}\n" \
          f"Najmniej dobrych ma lotnisko:{lotnisko_najgorsze}={min_dobrych}\n"

mb.showinfo("Komunikat",komentarz)

 

