#!/bin/python3

import os

nagusia = str(input("Sartu karpetak egingo diren bidea: "))
izena = str(input("Sartu karpetaren izena: "))
errepikapenak = int(input("Sartu errepikapenak: "))

for i in range(1, errepikapenak + 1):
	bidea = nagusia + "/" + izena + str(i)
	os.mkdir(bidea)
