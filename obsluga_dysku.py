import os
print(os.getcwd())
#print(os.listdir())

if os.path.exists("dane_Wielkopolskie.csv"):
    os.remove("dane_Wielkopolskie.csv")
    print("Plik bezpiecznie usuniety.")
else:
    print("Spokojnie, pliku juz nie ma.")