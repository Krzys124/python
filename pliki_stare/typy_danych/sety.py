

print("Sety, zestawy, zbiory")

#tworzenie - duplikaty są usuwane

owoce = {"jabłko", "banan", "wiśnia", "jabłko"}
print(owoce)

pusty_zbior = set()

#w zbiorach nie ma kolejnosci, indeksow

#dodawanie
owoce.add("mango")
print(owoce)

numery = [1, 2, 2, 3, 4, 4, 4, 5]
unikaty = list(set(numery))
print(numery)
print(unikaty)