cars=["Audi","BMW","Skoda","Kia"]
for car in cars:
    print("Pojazd: ", car)


#alternatywa

ile_razy=len(cars)
for element in range(ile_razy):
    print(f"Pobieram element: {element+1} tablicy o wartosci: {cars[element]}")

#alternatywa bez smieciowej zmiennej = 0 
for ile, car in enumerate(cars,start=0):
    print("Pojazd nr =",ile,end=" ")
    print("to: ",car)

garaz={
    "Toyota":"Corolla",
    "Mazda":"CX-5",
    "BMW":"M3",
    "Tesla":"Model S"
}

print("\n--- MOJA KOLEKCJA ---")
for marka, model in garaz.items():
    print(f"Marka: {marka} | Model: {model}")

print("\n--- POSIADANE MARKI ---")
for marka in garaz.keys():
    print(f"Mam w garazu samochod marki: {marka}")
    pojazd=garaz[marka]

print("\n--- POSIADANE MODELE ---")
for model in garaz.values():
    print(f"Mam w garazu pojazd: {model}")
    pojazd=garaz[marka]

auta_szczegoly={
    "WA12345":{"marka":"Toyota","rok":2020,"przebieg":50000},
    "KR67890":{"marka":"BMW","rok":2018,"przebieg":120000}
}

for rejestracja, dane in auta_szczegoly.items():
    print(f"\nAuto o numerze rej. {rejestracja}:")

    marka=dane["marka"]
    rok=dane["rok"]
    przebieg=dane["przebieg"]

    print(f" ->{marka} z roku {rok} ma przebieg: {przebieg}")


    