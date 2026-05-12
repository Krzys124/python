
print("słowniki, definiuje się w klamrach")

dict = {"brand":"Ford", "model":"Mondeo","year":2018, "color":"biały"}
print(dict)

#nie ma indeksow, sa nazwy kluczy
print(dict["model"])

#wartosc ze slownika przy pomocy get()
#get daje furtke bezpieczenstwa w przypadku pomylenia nazwy klucza
print(dict.get("model_auta","nie ma takiego klucza"))




