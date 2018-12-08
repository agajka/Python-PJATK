# -*- coding: utf-8 -*-

waga = float(input("Ile kilogramów ważysz? ",))
wzrost = float(input("Jaki jest twój wzrost w metrach [format: m.mm]? ",))
BMI = waga/(wzrost**2)
print("Twoje BMI wynosi: %f" % BMI)