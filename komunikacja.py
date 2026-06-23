#pobranie wartosci od usera

#imie=input("Podaj swoje imie:")
#print("Witaj,",imie,"!")


cena=input("Podaj cene pojazdu:")
if cena =="":
    print("Nie podano cenu pojazdu")
    exit()
elif not cena.isdigit():
    print("Podaj poprawna cene pojazdu")
    exit()
else:
    marka_pojazdu=input("Podaj marke pojazdu:")
    marka_pojazdu=marka_pojazdu.capitalize()

if marka_pojazdu=="":
    print("Nie podano marki pojazdu!")
    exit()

if marka_pojazdu=="Opel":
    rabat=.85
elif marka_pojazdu=="Skoda":
    rabat=.82
elif marka_pojazdu=="Audi":
    rabat=.8
else:
    rabat=.95

cena=int(cena)
print("Cena pojazdu wynosi:",cena*rabat)