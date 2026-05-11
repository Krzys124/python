import cowsay

print ("Siema siema!")
print ("1 2 3")
#coś

cowsay.cow("Muuuuuuuu!!")
print(cowsay.char_names)

# cowsay.cheese("AAAAAAaaaAAaaaa!!")
# cowsay.pig("AAAAAAaaaAAaaaa!!")
# cowsay.fox("AAAAAAaaaAAaaaa!!")
# cowsay.kitty("AAAAAAaaaAAaaaa!!")
# cowsay.miki("AAAAAAaaaAAaaaa!!")
# cowsay.octopus("AAAAAAaaaAAaaaa!!")

for i in cowsay.char_names:
    #cowsay.draw("aa AA aaaa AAA", i)
    print(cowsay.get_output_string(i, "aaaa AAAA aa AAa"))


print ("ala", "ma", "kota")
print ("ala"+"ma"+"kota")
print("***************************")
print ("ala"+"ma"+\
       "kota")

print ("*" * 40)



