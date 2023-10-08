import math
a = float(input("entrer la valeur de a :"))
b = float(input("entrer la valeur de b :"))
c = float(input("entrer la valeur de c :"))
delta = b ** 2 - 4 * a * c
if delta < 0 :
print("pas de solutions réelles")
elif delta == 0 :
x = (-b)/(2*a)
print("la solution est :";x)
else :
x1 = (-b-math.sqrt(delta))/(2*a)
x2 = (-b+math.sqrt(delta))/(2*a)
print("les solutions sont :",x1 "et",x2)
