krotka=(5,10,15,20,25)

jeden_element=("to",) #jeden element krotki - zakonczenie przecinkiem

print(jeden_element)
print(type(jeden_element))

print(len(krotka))

#konkatenacja krotek
k1=(1,2)
k2=(3,4)
wynik=k1+k2

#powielanie
owoce=("jablko")
print(owoce*5)

#sprawdzani obecnosci
liczby=(10,20,30,20)
print(20 in liczby)

lista=list(krotka)
lista[0]="nowy"
lista=tuple(lista)
print(type(lista))

