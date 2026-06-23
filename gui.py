from tkinter import simpledialog
from tkinter import messagebox
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER

odpowiedz=messagebox.askyesnocancel("Wlaczenie programu","Czy na pewno chcesz wlaczyc program?")
if odpowiedz==True:
    print("wcisnieto tak")
elif odpowiedz==False:
    print("wcisnieto nie")
else:
    print("wcisnieto anuluj")

tabela=PrettyTable()
tabela.field_names=["Marka","Rabat"]
tabela.add_row(["Opel","15%"])
tabela.add_row(["Skoda","18%"])
tabela.add_row(["Audi","20%"])
tabela.add_row(["Inne","5%"])
tabela.set_style(DOUBLE_BORDER)
print(tabela)

cena=simpledialog.askfloat("Cena pojazdu","Podaj cene pojazdu:",minvalue=1,maxvalue=300000)
if type(cena)!=float:
    messagebox.showerror("Error","fatal error")
marka_pojazdu=simpledialog.askstring("Marka pojazdu","Podaj marke pojazdu:")
marka_pojazdu=marka_pojazdu.capitalize()

if marka_pojazdu=="Opel":
    rabat=.85
elif marka_pojazdu=="Skoda":
    rabat=.82
elif marka_pojazdu=="Audi":
    rabat=.8
else:
    rabat=.95

cena=int(cena)
messagebox.showinfo("obliczenia","Cena pojazdu wynosi: "  +  str(cena*rabat))