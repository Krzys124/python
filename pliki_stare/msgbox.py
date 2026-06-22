
from tkinter import messagebox
#messagebox.showinfo("Info moje", "Jakiś komunikat")
#messagebox.showwarning("Uwaga uwaga", "Pociąg odjeżdża")
#messagebox.showerror("aaaa aaa aa", "Pali się!!")

marka = input("Podaj marke pojazdu: ").lower()

if marka != "":
    odpowiedz = messagebox.askyesno("Uawga, szlachta pyta", "Czy chcesz obliczyć rabat dla "+marka)

    if odpowiedz:
        if marka == "opel":
            rabat = 0.15
        elif marka == "skoda":
            rabat = 0.18
        elif marka == "audi":
            rabat = 0.20
        else:
            rabat = 0.05

        messagebox.showinfo("Rabacik dla Pana", f"Cena po rabacie: {100000*(1-rabat):,.0f}zł")
    else:
        messagebox.showinfo("Uuuuuuu", "Nie to nie, ić stąd!")

else:
    messagebox.showinfo("A marka to gdzie?", "Nie ma marki - nie ma rabatu")


