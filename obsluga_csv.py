import csv

with open("dane.csv",mode="r",encoding="utf8") as plik:
    czytnik=csv.DictReader(plik,delimiter=";")
    
    for wiersz in czytnik:
        print(f"Pojazd: {wiersz['Marka pojazdu']}, Cena: {wiersz['Cena netto']}")
