


cars = ['audi', 'mercedes', 'skoda', 'kia', 'fiat']

for car in cars:
    print(f"Marka: {car}")


for u in (0,1,2,3,4):
    print(f"Krok: {u}")

for u in range(5):
    print(f"Krok: {u}")

for u in range(10,20,2):
    print(f"Krok: {u}")


ile_razy = 6

for i in range(ile_razy):
    print(f"Krok petli: {i}")
    y=i*2
    print(f"y=",y)



for car in range(len(cars)):
    print("Pojazd nr = ", car, end=" ")
    print("to:", cars[car])



garaz = {
    "Toyota": "Corolla",
    "Mazda": "CX-5",
    "BMW": "M3",
    "Tesla": "Model S"
         }


for marka, model in garaz.items():
    print(f"Marka: {marka} | Model: {model}")

for marka in garaz.keys():
    print(f"Mam samochód marki: {marka} {garaz[marka]}")


for marka in garaz.values():
    print(f"Mam samochód : {marka}")




flota = {
    "WA1298J": {"marka": "Toyota","rok": 2024,"przebieg":50000},
    "KNS1568P": {"marka": "Ford","rok": 2020,"przebieg":250000}
         }


for rejestracja, dane in flota.items():
    print(f"Auto o numerze rejestracyjnym {rejestracja}")

    marka = dane["marka"]
    rok = dane["rok"]
    przebieg = dane["przebieg"]

    print(f"  -> {marka} z roku {rok} ma przebieg {przebieg}")





print(3 * "*\n")
print("zagnieżdżanie pętli for")

X = ['a', 'b', 'c']
Y = [1, 2, 3, 4]

for i in X:
    for j in Y:
        print(f"Komurka {i.upper()}{j}")


print(3 * "*\n")
print("pętla while")  

licznik = 0
while licznik < 5:
    print(f"Licznik: {licznik}")
    licznik += 1



#instrukcje sterowanie pętlami: break, continue, else
cars = ['audi', 'mercedes', 'skoda', 'kia', 'fiat']
szukam = 'skoda'

for i in cars:
    if i == szukam:
        print(f"Znalazłem {szukam} na liście")
        break
else:
    print(f"Nie ma {szukam} na liście")
