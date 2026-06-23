pensja=7000
wczasy="mazury"

if pensja <5000 and wczasy=="mazury":
    komunikat="nie za wiele"
# \ podzial wiersza na kilka linii
elif (pensja <8000 and 
    (wczasy=="mazury" or wczasy=="morze")):
    komunikat="moze byc"
elif pensja <13000 and pensja >= 8000:
    komunikat="super"
else:
    komunikat="nie jest zle"

#komunikaty
print(komunikat)