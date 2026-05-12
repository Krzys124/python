
# imie = input("Podaj imie: ")

# print(f"Witaj, {imie}!")

# wiek = input("Ile masz lat? ")
# print(f"Za 3 lata będzisz miał {int(wiek)+3}")


marka = input("Podaj marke pojazdu: ").lower()



if marka != "":

    if marka == "opel":
        rabat = 0.15
    elif marka == "skoda":
        rabat = 0.18
    elif marka == "audi":
        rabat = 0.20
    else:
        rabat = 0.05

    print(f"Rabat dla marki {marka.title()} wynosi {rabat*100:,.0f}%")
    print(f"Cena po rabacie: {100000*(1-rabat):,.0f}zł")
else:
    print("Pana nie obsługujemy!!!!")

