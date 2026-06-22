zamiana="Ala ma kota".replace("kota","misia")
duze_znaki=zamiana.upper()
print(duze_znaki)
test=zamiana.find("misia")
print(test)
test2=zamiana.capitalize
print(test2)


tekst_CSV="03/22/2025 jan KOWalski wyplata PLN: 8359"
data=tekst_CSV[3:5] + "-" + tekst_CSV[0:2] + "-" + tekst_CSV[6:10]
print(data)

position_wyplata=tekst_CSV.find("wyplata")
#print(position_wyplata)
imie_nazwisko=tekst_CSV[11:position_wyplata].title()
print(imie_nazwisko)

kwota=tekst_CSV[position_wyplata+13:]
#kwota_euro=int(kwota)*4.33
print(kwota,"PLN")
print(f"{(int(kwota)/4.33):.2f}","EURO")

imie_nazwisko=tekst_CSV[11:position_wyplata].replace("jan","marek").replace("KOWalski","pieKNy").title()
print(imie_nazwisko)
print(kwota.replace("8359","10999.76"),"PLN")
print(f"{(float(kwota.replace("8359","10999.76"))/4.33):.2f}","EURO")
