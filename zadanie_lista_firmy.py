#import
from tkinter import simpledialog
from tkinter import messagebox
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER

#import
from dane_firmy_kursy import firmy, Kurs_akcji_dzis, Kurs_akcji_wczoraj


#dane
# 1. wersja
#firmy = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7","Firma 8"]
#Kurs_akcji_wczoraj = [16.48, 25.24,57.23,37.92,99.59,94.39,91.56,100.0]  
#Kurs_akcji_dzis    = [16.71,25.64 ,57.11, 38.16, 99.14, 94.52, 91.11,110.0]


ilosc=len(Kurs_akcji_dzis)
aktualna_wartosc=[]
info=[]
tabela=PrettyTable()
tabela.field_names=["Firma","Kurs wczoraj","Kurs dzisiaj","Wartosc","Informacja"]
tabela.set_style(DOUBLE_BORDER)
komunikat_do_mb=""


for element in range(ilosc):
    wartosc=Kurs_akcji_dzis[element]-Kurs_akcji_wczoraj[element]
    #print(f"{wartosc:.2}")
    aktualna_wartosc.append(f"{wartosc:.2}")
    if wartosc<0:
        informacja="spadl"
    else:
        informacja="wzrosl"
    info.append(informacja)
    tabela.add_row([firmy[element],Kurs_akcji_wczoraj[element],Kurs_akcji_dzis[element],aktualna_wartosc[element],info[element]])
    firma=firmy[element]
    info2=info[element]
    aktualna_wartosc2=aktualna_wartosc[element]
    komunikat=f"Firma: {firma},kurs akcji {info2} o {aktualna_wartosc2}"
    komunikat_do_mb+=komunikat+"\n"
#print(aktualna_wartosc)
#print(info)

messagebox.showinfo("Informacja",komunikat_do_mb)

print(tabela)