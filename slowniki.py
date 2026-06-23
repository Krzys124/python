dict={
    "brand":"Ford",
    "model":"Mondeo",
    "year":2018
}
print(dict)
print(type(dict))

print(dict["model"])

x=dict["model"]

x=dict.get("model")
x=dict.get("model_auta","brak danych")
print(dict.get("model_auta","brak danych"))

dict["year"]=2023           #podmiana
dict["kolor"]="czarny"      #dodanie nowej wartosci
print(dict)

mapa={
(52.2,21.0):"Warszawa",
(35.4,11,34):"Lodz",
(34.32,11,45):"Wroclaw"
}
#print(mapa)

print(mapa.keys())          #zwraca liste nazw kluczy
print(mapa.values())        #zwraca liste samych wartosci
print(mapa.items())         #$zwraca liste par (klucz i wartosc)

