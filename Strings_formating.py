# -*- coding: utf-8 -*-
"""
waga = float(input("Ile kilogramów ważysz? ",))
wzrost = float(input("Jaki jest twój wzrost w metrach [format: m.mm]? ",))
BMI = waga/(wzrost**2)
print("Twoje BMI wynosi: %f" % BMI)


print("1 po angielsku: \t%s \n2 po angielsku: \t%s" % ('one', 'two'))

print("1 po angielsku: {} \n2 po angielsku: {}".format('one', 'two'))

print("100 to {} \n200 to {}".format('hundred','two hundreds'))

print("{:.2f} to hundred \n{:f} means two hundreds".format(100,200))

print("Rekord świata na 100m to {:.2f} ustanowił go {}".format(9.58, 'Usain Bolt'))

print("Kiedy się urodziłes?")
print("Rekord świata na 100m padł {} i wynosi poniżej {:.1f} sekund - wow!".format(input(), 9.58))


szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.3f} | {:16s} | {:10s} |".format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.745, "Asafa Powell", "2.09.2008"))
print("-" * szer)



waluta = "dolar"
us = 1
pln = 4.08234915
print("Aktualnie {} {} kosztuje {:.2f} zł".format(us, waluta, pln))



print("{} ma {}".format("Ala", "kota"))
print("{1} ma {0}".format("Ala", "kota"))


cm = float(input("Ile chciałbyś mieć centymetrów? ",))
print("Czy jesteś pewien, że chciałbyś mieć {:.4f} metrów, czyli {:.4f} cali?".format(cm/100,cm*0.39370))

"""

print("Witaj w kalkulatorze do obliczania stopy zwrotu z lokaty, uwzględniający miesięczną kapitalizację odsetek.")
sp = float(input("\nPodaj stan początkowy konta: "))
opr = float(input("Podaj stopę oprocentowania rocznego [%]: "))
dl = float(input("Podaj długosc lokaty w latach: "))

zysk = sp*(1+((opr/100)*0.81)/12)**(12*dl)

print("\nTwoje {:} złotych przez {:.0f} lat(a) na lokacie z {:} % oprocentowaniem urosnie do {:.2f} (uwzględniając podatek Belki)".format(sp, dl, opr, zysk))