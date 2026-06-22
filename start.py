#kmunikacja - olecenie print
"""
no 
to
wiekszy
komentarz
"""

print("czesc","Rafal")
print("czesc"+" Rafal") #konkatenacja tekstow
print("*"*60)

#zmienne
imie="Rafal"
print("Czesc",imie)

#import keyword
#print(keyword.kwlist)
#definiowanie kilku zmiennych na raz
x,y,z=1,4,345.68854896487988757
print(x,y,z)

x=5
y=5.25
z=True

q=x+int(y)
print(q)

a=16.48
b=16.71
c=a-b
print(c)
print(f"{c:.2f}")
c=round(c,2)
print(c)


print("jestem na szkoleniu",F"Imie:{imie}",sep=".")
print("jestem na szkoleniu",end=".")
print(F"Imie:{imie}")

x=5
x+=1
print(x,type(x))

a="chleb"
b="maslo"

print(F"Lista zakupow: \n\t {a} \n\t {b}")

liczba=1232443346.45654743734
print(f"Wynik: {liczba:,}")

t1="Ala ma kota"
t2=t1.replace("Ala","Zuzia")
print(t2)

print(f"Wynik: {liczba:_}".replace(".",",").replace("_"," "))