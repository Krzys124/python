



#instrukcja if

a = -3
if a > 0:
    print("Zmienna dodatnia")
else:
    print("Zmienna ujemna")


temp = 35
if temp > 30:
    print("Gorąco!!")
elif temp > 15:
    print("Ciepło")
elif temp > 5:
    print("Chłodno")
else:
    print("Zimno")



if temp >= 15 and temp < 30:
    print("Ciepło")
elif temp > 5 and temp < 15:
    print("Chłodno")
elif temp < 5:
    print("Zimno")
else:
    print("Gorąco!!")



# nieoczywiste operatory logiczne: is, in, not



print('str' is 'string')

