from datetime import datetime, date

tekst_csv = "03/12/2025 jan KOWalski wypłata PLN: 8359"

pozycja = tekst_csv.find("wypłata")
imie_nazwisko = tekst_csv[11:pozycja].title()

print(f"{imie_nazwisko}")

dd = int(tekst_csv[0:2])
mm = int(tekst_csv[3:5])
rr = int(tekst_csv[6:10])

print(f"dzień: {dd}, miesiąc: {mm}, rok: {rr}")

data_z_tekstu = tekst_csv[0:10]
data_obiekt = datetime.strptime(data_z_tekstu, "%d/%m/%Y")  #parsowanie daty
print(f"\nData jak z pliku: {data_obiekt}")
data_obiekt = datetime.strftime(data_obiekt,"%Y.%m.%d")     #formatowanie daty
print(f"Data po sformatowaniu: {data_obiekt}")

pozycja = tekst_csv.find(":")
wyplata_pln = float(tekst_csv[pozycja + 2:])

print(f"\nwyplata PLN: {wyplata_pln:,.2f}")
print(f"wyplata EUR: {wyplata_pln*4.33:,.2f}")
