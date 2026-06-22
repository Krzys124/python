from datetime import datetime, date, timedelta
teraz=datetime.now()
print(f"Teraz jest:,{teraz}")
print("Teraz jest:",teraz)

urodziny=date(1995,10,25)
print(f"Urodziny:{urodziny}")

przyszlosc=teraz+timedelta(days=100)
print(przyszlosc)

teraz=datetime.now().date()

wynik_dni=(teraz-urodziny).days
print("Dni, ktore minely:",wynik_dni)

tekst_CSV="03/22/2025 jan KOWalski wyplata PLN: 8359"
dzien=int(tekst_CSV[3:5])
miesiac=int(tekst_CSV[0:2])
rok=int(tekst_CSV[6:10])

print(rok,miesiac,dzien)
data=date(rok,miesiac,dzien)
print(data)

szkolenie_BHP=data+timedelta(days=270)
print("Data szkolenia BHP:",szkolenie_BHP)

szkolenie_BHP=szkolenie_BHP.strftime("%d.%m.%y")
print("Data szkolenia BHP:",szkolenie_BHP)

data_z_pliku="2026-12-31"
obiekt_daty=datetime.strptime(data_z_pliku,"%Y-%m-%d")
print(obiekt_daty)