mieszana=["Ania",25,True]

print(mieszana[-1])

#dlugosc=mieszana.len()
#print(dlugosc)



lista=[5,10,15,20,25]
print(sum(lista))

tekst_CSV="03/22/2025 jan KOWalski wyplata PLN: 8359"
pasek_wyplaty=tekst_CSV.split()
#print(pasek_wyplaty)

pasek_wyplaty.append([10000,15000])
print(pasek_wyplaty)
pasek_wyplaty.extend([10000,15000])
print(pasek_wyplaty)
