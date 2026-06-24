from prettytable import PrettyTable as pt, DOUBLE_BORDER
import os

#pomocnicze zmienne
pojazdy={}
# tbl=pt()
# tbl.field_names=["Marka","Ile","Suma","Sredni przebieg"]


#odczyt
with open(r"dane.csv","rt",encoding="utf8") as plik:

#odczytanie 1 wiersza - przesuniecie kursona na wiersz 2
    naglowki=plik.readline()
#odczyt danych wiersz po wierszu
    for wiersz in plik:
        lista_rekord=wiersz.strip().split(";")
        marka=lista_rekord[1]
        lokalizacja=lista_rekord[7]
        
        if lokalizacja not in pojazdy:
            pojazdy[lokalizacja]={}

        if marka not in pojazdy[lokalizacja]:
            pojazdy[lokalizacja][marka]={"suma_cen:":0,"sredni_przebieg":0,"ile":0}
        #slownik=pojazdy[marka]
        #slownik["ile"]+=1

        pojazdy[lokalizacja][marka]["ile"]+=1
        pojazdy[lokalizacja][marka]["suma_cen:"]+=float(lista_rekord[2])
        pojazdy[lokalizacja][marka]["sredni_przebieg"]+=float(lista_rekord[8])

print(pojazdy)        
    #dodanie wierszy
for lokalizacja in pojazdy.keys():
    
    tbl=pt()
    tbl.field_names=["Marka","Ile","Suma","Sredni przebieg"]
    for m in pojazdy[lokalizacja].keys():
        pojazdy[lokalizacja][m]["sredni_przebieg"]=round(pojazdy[lokalizacja][m]["sredni_przebieg"]/pojazdy[lokalizacja][m]["ile"],2)
        tbl.add_row([m,pojazdy[lokalizacja][m]["ile"],
                     pojazdy[lokalizacja][m]["suma_cen:"],
                     pojazdy[lokalizacja][m]["sredni_przebieg"]])
    #print(tbl)
#nie zamykamy pliku, bo konstrukcja with sama go zamyka

    folder_wynikowy=r"C:\Users\Szkolenie_03\Documents\cwiczenia\wyniki"
    if not os.path.exists(folder_wynikowy):
        os.makedirs(folder_wynikowy)

    nazwa_pliku="dane_"+lokalizacja+".csv"
    with open(nazwa_pliku,"w",encoding="utf8") as plik:
        # for m in pojazdy.keys():
        #     plik.write("pojazd: "+m+" ile: "+str(pojazdy[m])+"\n")



            plik.write("-------------------------------dane z prettytable-------------------------------\n")
            plik.write(str(tbl))
                
            plik.write("-------------------------------dane z prettytable jak csv-------------------------------\n")
            plik.write(tbl.get_csv_string())

#zapisz w kolejnym nowym pliku informacje o sumie cen marki pojazdu i info o srednich przebiegach


#Przygotuj tyle plikow ile wojewodztw, zapisz obliczenia w kontekscie kazdego wojewodztwa
