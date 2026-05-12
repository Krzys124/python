

owoce = ["jabłko", "banan", "wiśnia"]
liczby = [1, 2, 5, 5, 10]
mieszana = ["Ania", 25, True, None]


#dostep do elementow
print(owoce[0])
print(owoce[-1])

#podmiana elementow 
owoce[0] = "gruszka"
owoce[1] = "śliwka"
owoce[2] = "arbuz"

print(owoce[0])
print(owoce[-1])


print (owoce)
owoce.append("kiwi")
owoce.insert(1,"mango")
print(owoce)
owoce.remove("arbuz")
print(owoce)

print(mieszana)
mieszana.extend(owoce)
print(mieszana)

A = [1, 2]
print(A)

B = [3, 4]
B.append(A)
print(B)
B.extend(A)
print(B)



print("\nĆwiczenie: wyciągnąć z tekstu dane jako elementy listy:")
tekst_csv = "03/12/2025 jan KOWalski wypłata PLN: 8359"
lista_z_tekstu = tekst_csv.split(" ")
print(lista_z_tekstu)
print(f"Imię: {lista_z_tekstu[1].title()}, nazwisko: {lista_z_tekstu[2].title()}")

print("\nĆwiczenie: tekst z listy:")
list = ["Ala", "ma", "kota"]
tekst_z_listy = " ".join(list)
#przed kropką separator, ktory połączy elementy listy
print(f"Tekst z listy: {tekst_z_listy}")

print("\nĆwiczenie: podmienić imię w tekście:")
tekst = " ".join(list).replace("Ala", "Zuzia")
print(f"Tekst z podmienionym imieniem: {tekst}")



print("\nĆwiczenie: listy wielowymiarowe:")

macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(macierz)
print(macierz[0])
print(macierz[1][1])

macierz[2][2]=10
print(macierz)

macierz[1].append("kamień")
print(macierz)

macierz[2].remove(7)
print(macierz)

print(f"Ilosc elementow macierzy: {len(macierz)}")
for i in range(len(macierz)):
    print(f"Dlugosc elementu {i}: {len(macierz[i])}")



print("\nĆwiczenie: referencje: zastąpienie zmiennej inną wartością")
print("test 1:")
x=5
y=x
print(y)

x=10
print(y)


#################3
print("test 2: zastąpienie jednego wyrazu innym")
x="abc"
y=x
print(y)

x="XYZ"
print(y)

#################3
print("test 3: zastąpienie jednej listy inną listą")
x=["a", "b", "c"]
y=x
print(y)

x=[1, 2, 3]
print(y)


#################3
print("test 4: referencja do listy")
x=["a", "b", "c"]
y=x
print(y)

x.append("v")
print(y)


#################3
print("test 5: kopia listy")
x=["a", "b", "c"]
y=x.copy()
print(y)

x.append("v")
print(y)