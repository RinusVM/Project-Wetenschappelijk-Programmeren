# -*- coding: utf-8 -*-
"""
TEMPLATE VOOR PROJECT WETENSCHAPPELIJK PROGRAMMEREN

Academiejaar 2023-2024

Vul deze template aan (en dien deze in via Ufora)

Groepsleden:    Groepslid 1: .......
                Groepslid 2: .......
                Groepslid 3: .......
                Groepslid 4: .......

"""
import infoFun

########################################################
#%% Opdracht 2. uitgebreide controle op bitstring
########################################################

def isGeldig(bitstring):
    # vul aan 
    pass


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

