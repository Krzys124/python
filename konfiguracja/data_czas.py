from datetime import datetime, date, timedelta

teraz = datetime.now()
teraz2 = datetime.now().date()
teraz3 = datetime.now().time()

godz = teraz.hour
minuty = teraz.minute
sekundy = teraz.second

rr = teraz.year
mm = teraz.month
dd = teraz.day

print(f"Teraz jest: {teraz}, sama data: {teraz2}, sam czas: {teraz3}")
print(f"Gdziny: {godz}, minuty: {minuty}, sekundy: {sekundy}")
print(f"Dzień: {dd}, miesiąc: {mm}, rok: {rr}")

dz_tyg = ["PN", "WT", "ŚR", "CZW", "PT", "SO", "ND"]

print(f"Dzień tygodnia: {dz_tyg[teraz.weekday()]}") #0 - poniedziałek, 6 - niedziela

urodziny = date(1995,10,25)
print(f"\nUrodziny: {urodziny}")


#co będzie za 100 dni
przyszlosc = teraz + timedelta(days=100)
print(f"\nZa 100 dni będzie: {przyszlosc}")

#objekt -> tekst
format_euro = teraz.strftime("%d.%m.%Y %H:%M")
print(f"\nFormat europejski: {format_euro}")

#tekst -> objekt
data_z_pliku = "2026-12-11"
obiekt_daty = datetime.strptime(data_z_pliku, "%Y-%m-%d")
print(f"data z pliku: {obiekt_daty}")

