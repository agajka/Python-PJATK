# -*- coding: utf-8 -*-

print("Witaj w kalkulatorze do obliczania stopy zwrotu z lokaty, uwzględniający miesięczną kapitalizację odsetek.")
sp = float(input("\nPodaj stan początkowy konta: "))
opr = float(input("Podaj stopę oprocentowania rocznego [%]: "))
dl = float(input("Podaj długosc lokaty w latach: "))

zysk = sp*(1+((opr/100)*0.81)/12)**(12*dl)

print("\nTwoje {:} złotych przez {:.0f} lat(a) na lokacie z {:} % oprocentowaniem urosnie do {:.2f} (uwzględniając podatek Belki)".format(sp, dl, opr, zysk))