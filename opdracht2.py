# -*- coding: utf-8 -*-
"""
TEMPLATE VOOR PROJECT WETENSCHAPPELIJK PROGRAMMEREN

Academiejaar 2023-2024

Vul deze template aan (en dien deze in via Ufora)

Groepsleden:    Groepslid 1: Ghita Alexander
                Groepslid 2: Vandekerckhove Laurika
                Groepslid 3: Van Massenhove Rinus 
                Groepslid 4: Vranken Katelijne

"""
import infoFun

########################################################
#%% Opdracht 2. uitgebreide controle op bitstring
########################################################


def isGeldig(bitstring):
    geldig = True
    errors = []
    lengte = len((bitstring))

    if lengte < 22:
        geldig = False
        errors.append("De lengte van de string moet minstens 22 zijn.")

    isBinairy = True     
    for i in bitstring: 
        if i != "0" and i != "1":
            geldig = False
            isBinairy = False 
    if isBinairy == False:
        errors.append("De string bestaat enkel uit de karakters '0' en '1'.")
   
    if (lengte - 8) % 14 != 0:
        geldig = False
        errors.append("De lengte van de string verminderd met 8 moet een veelvoud zijn van 14.")
   
    if bitstring[0:4] != "1010":
        geldig  = False
        errors.append("De string begint niet met het startsymbool 1010")

    if bitstring[-4:] != "1101":
        geldig  = False
        errors.append("De string eindigt niet met het eindsymbool 1101")

    for i in range(len(bitstring)):
        if bitstring[i:i+3] == "000" or bitstring[i:i+3] == "111":
            geldig  = False
            errors.append("Het aantal opeenvolgende 0'en en 1's is groter dan twee.")
    return geldig

# test code
controle1  = isGeldig("1010110100100101101101") # geldige bitstring
print(controle1)

controle2  = isGeldig("10101101001001XX101101") # ongeldige karakters
print(controle2)

controle3  = isGeldig("1010110111100101101101") # "1" komt meer dan 2 keer voor
print(controle3)

controle4  = isGeldig("1101110100100101101010") # start/eindsymbool verkeerd
print(controle4)

controle5  = isGeldig("10101101001011010110101101") # geen veelvoud van 14
print(controle5)
