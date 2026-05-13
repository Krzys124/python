
from tkinter import messagebox, simpledialog

ceny_pln = [45000, 120000, 32500, 89900, 5500]
suma = sum(ceny_pln)
srednia = suma/len(ceny_pln)
przelicznik = 1.0
waluta = "PLN"

odpowiedz = messagebox.askyesno("Pytanie do użytkownika", "Czy wyświetlić ceny w euro?")

if odpowiedz:
    print("Tak, ceny w euro")
    kurs = simpledialog.askfloat("Kurs", "Podaj kurs euro")
    print(f"Kurs: {kurs}")
    waluta = "EUR"
    przelicznik = kurs

    #ceny_eur2 = [ x*2 for x in ceny_pln]
    
wiadomosc = f"Kurs: {przelicznik},\n" \
    f"Suma w {waluta}: {suma*przelicznik:,.2f}\n" \
        f"Cena śrenida w {waluta}: {srednia*przelicznik:,.2f} "

messagebox.showinfo(f"Ceny w {waluta}", wiadomosc)
#messagebox.showinfo("Ceny w Euro", f"Kurs: {kurs},\nSuma w euro: {suma*kurs:,.2f}\nCena śrenida w euro: {srednia*kurs:,.2f} ")





