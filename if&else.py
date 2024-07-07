# if-else statements
a = int(input("enter your age: "))
print("your age is:",a)

if(a>18):
    print("you can drive")

else:
    print("you cannot drive")


applePrice = 250
buget =  45
if ( applePrice <= buget):
    print("Alexa add 1 kg Apples to the cart")

elif (buget - applePrice > 50):
   print("its okay you can buy")
       

else:
    print("Alexa,do not add Apples to the cart.")


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")