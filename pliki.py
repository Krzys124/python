#otwarcie pliku
plik=open(r"dane_tekstowe.txt","rt",encoding="utf8")
#odczyt calosci
zawartosc=plik.read()
print(zawartosc)


#restart kursora od poczatku pliku - czytam go jeszcze raz
plik.seek(0)

i=0
for wiersz in plik:
    print("WIERSZ",i,wiersz.strip())
    i+=1

#zamykanie pliku
plik.close()

#konstrukcja nie wymagajaca zamykania pliku
with open(r"dane_tekstowe.txt","rt",encoding="utf8") as plik:
    zawartosc=plik.read()
    print(zawartosc)

#append - dodanie danych do pliku
with open(r"dane_tekstowe.txt","a",encoding="utf8") as plik:
    plik.write("\nNowy tekst")