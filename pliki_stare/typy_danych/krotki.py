


print("Krotki = tuplety")
print("w innych jezykach = stałe, raz stworzone nie mogą być zmienione")
print("nie robimy pustej krotki")

krotka = ("Ala", 3, "koty")
print(krotka)
print(krotka[0])
print(krotka[1])

#w przypadku krokit jednoelementowej trzeba dać przecinek
krotka_jeden_element = ("dom",)



#krotka,lista ze zmiennych
x=2
y=3

lista = [x, y]
print(f"Lista ze zmiennych: {lista}")
krot = (x, y)
print(f"Krotka ze zmiennych: {krot}")


#krotka - rozpakowanie do zmiennych
a,b,c = krotka
print(f"Elementu krotki: {a}, {b}, {c}")
a = "Zuzia"
print(f"Elementu krotki: {a}, {b}, {c}")

#funkcje kroki
aaa = ("dom", "ulica", "blok", "ulica", "znak", "ulica")
print(f"Słowo ulica padło {aaa.count("ulica")} razy")
print(f"Słowo ulica wystąpiło na {aaa.index("ulica")} miejscu")
print(f"Czy słowo blok jeste w krotce: {"blok" in aaa}")


#łączenie krotek
k1 = (1,2)
k2 = (3,4)
k3 = k1 + k2
print(k3)
print(k1 * 3)


#zmiana krotki na liste
lista = list(aaa)
print(lista)
lista.append("nowy")
print(lista)





