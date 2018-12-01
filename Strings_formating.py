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

"""

szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.3f} | {:16s} | {:10s} |".format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.745, "Asafa Powell", "2.09.2008"))
print("-" * szer)