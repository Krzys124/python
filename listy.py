mieszana=["Ania",25,True]

#print(mieszana[-1])

#dlugosc=mieszana.len()
#print(dlugosc)



lista=[5,10,15,20,25]
#print(sum(lista))

tekst_CSV="03/22/2025 jan KOWalski wyplata PLN: 8359"
pasek_wyplaty=tekst_CSV.split()
#print(pasek_wyplaty)

pasek_wyplaty.append([10000,15000])
#print(pasek_wyplaty)
pasek_wyplaty.extend([10000,15000])
#print(pasek_wyplaty)


macierz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(macierz[2][1])

macierz[0].append(4)
print(macierz)

print(len(macierz))
print(len(macierz[0]))
print(len(macierz[1]))

