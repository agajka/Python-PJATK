"""
#Zad. 1
print("Ile masz lat?")
age = int(input())
if age >= 18:
    print("Jestes pełnoletni.")
if age > 100:
    print("To naprawdę Twój wiek? 200 lat ♫.")
else:
    print("Zostalo Ci do pelnoletnosci lat:", 18-age)
 
#Zad. 2
waga = float(input("Ile kilogramów ważysz? ",))
wzrost = float(input("Jaki jest twój wzrost w metrach [format: m.mm]? ",))
BMI = waga/(wzrost**2)
print("\nTwoje BMI wynosi: ", round(BMI, 2))

if BMI < 18.5:
    print("Niedowaga")
elif (18.5 <= BMI < 24):
    print("Waga prawidłowa")
elif (24 <= BMI < 26.5):
    print("Lekka nadwaga")
else:
    print("Nadwaga")
    if (30 <= BMI < 35):
        print("Otylosć I stopnia")
    elif (35 <= BMI < 40):
        print("Otylosć II stopnia")
    elif (40 <= BMI):
        print("Otylosć III stopnia")
  """ 
#Zad. 3
print("Podaj liczbę x:")
x = float(input())
print("Podaj liczbę y:")
y = float(input())
print("Podaj liczbę z:")
z = float(input())

if (x>y)and (x>z):
    maksimum = x
elif (y>x) and (y>z):
    maksimum = y
else:
    maksimum = z
    
print("Największa z liczb: ", maksimum)

if x < y:
    temp = x
    x = y
    y = temp
if x < z:
    temp = x
    x = z
    z = temp
if y < z:
    temp = y
    y = z
    z =temp
print ("Liczby w kolejnosci malejacej to {}, {}, {}.".format(x , y, z))