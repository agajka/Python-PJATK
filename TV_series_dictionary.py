"""
#1
quote='''To jest wielolinijkowy tekst zawierający cytat "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live" -John Wood'''
print(quote)

#2
print('czeko', end=' ') 
print('lada', end='')

#3
txt = r"Nowe linie zapisujemy jako \n a tabulatory za pomocą \t"
print(txt)

#4
Lista = [3,5,"herbata", False]
print(Lista)
Lista[0] = 4
print(Lista)

#5
Krotka = (3,5,"kawa", True)
print(Krotka)
print(Krotka[2])

#6
Slownik = { "kawa": "czarna", "herbata" : "zielona", "cukier kostka": 4, 0: "zero"}
print(Slownik["herbata"])
print(Slownik[0])
Slownik[1] = "jeden"
print(Slownik[1])

print(Slownik.keys())
print(list(Slownik.keys()))
print(Slownik.values())

print("herbata" in Slownik)

#7
myVariable = 5
print(myVariable)
print(type(myVariable))
myVariable = 'tekst'
print(myVariable)
print(type(myVariable))

varA, varB, varC = 4,14,"kawa"


#Zad. 1
int = 4
print(4)
float = 4.4
print(float)
string = 'string'
print(string)
bool = True
print(bool)
lista = [3,"trzy",4.4,"cztery i cztery"]
print(lista)
tuple = (2, "dwa", 6.5, "szeć i pół")
print(tuple)
slownik = {"dzisiaj":"niedziela","dzień":2,12:"grudzień"}
print(slownik)
"""

#Zad. 2
seriale = {"SerialA":8,
           "SerialB":3,
           "SerialC":7.7,
           "SerialD":1
        }
print(list(seriale.keys()))

jaki = input("Jaki serial z listy chcesz obejrzeć? ")
print("Serial {} oceniony został na {}".format(jaki, seriale[jaki]))

nowy = input("Jaki nowy serial ostatnio obejrzałes? ")
ocena = input("Jak go oceniasz? ")
seriale[nowy]=float(ocena)
print()
print(list(seriale.keys()))