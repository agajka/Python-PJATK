# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:21:43 2018

@author: pd2876
"""

napis1="ciasto czekoladowe"
print(napis1)
print(len(napis1))

txt="hel lo"
print(txt[2:4])
txt=txt[0] + "a" + txt[2:]
seq = "ss"
print(txt.join(seq))
print(max(txt))

print(txt.split())

text = "ala ma kota"
print(text.replace(" ","-"))

print("Python Jest Fajny".istitle())


#Zad. 1
sentence = "Kurs Pythona jest prosty i przyjemny."
print(len(sentence))
print(sentence[18:25])
print(sentence[7])
print(sentence[12])
print(sentence[-4])
#print(sentence[37])

print(sentence[0:2] + "sz" + sentence [4:28] + "ż" + sentence[30:])