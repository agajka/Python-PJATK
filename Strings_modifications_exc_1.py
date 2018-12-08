# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:21:43 2018

@author: pd2876
"""

#Zad. 2
imie = input("Czesc! Jak masz na imię? ")
nazwisko = input("Witaj {}! Jakie jest twoje nazwisko? ".format(imie))
tel = input("{}, podaj proszę swój numer telefonu: ".format(imie))

#Ad. 1
#print("\n")
print("*"*52)
print("\nCzy Twoje imię składa się wyłacznie z liter? ", end="")
print(imie.isalpha())
print("\nCzy Twoje nazwisko składa się wyłącznie z liter? ", end="")
print(nazwisko.isalpha())
print("\nCzy Twój numer telefonu składa się wyłącznie z cyfr? ", end="")
print(tel.isdigit())

#Ad. 2
imie = imie.capitalize()
nazwisko = nazwisko.capitalize()

#Ad. 3
tel = tel.replace("-","")
tel = tel.replace(" ","")

#Ad. 4
kobieta = imie.endswith("a")
print("\nCzy jestes kobietą? {}".format(kobieta))

#Ad. 5
personal = imie + " " + nazwisko + " " + tel
print("\n\nTwoje dane personalne to: {}".format(personal))

#Ad. 6
print("\nLiczba wszystkich znaków w powyższym ciągu to: ", end = "")
print(len(personal))

#Ad. 7
l_liter = len(personal) - personal.count(" ") - len(tel)
print("\nLiczba liter w danych to: " + str(l_liter))