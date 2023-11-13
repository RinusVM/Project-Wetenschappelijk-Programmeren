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

########################################################
#%% Opdracht 1. bitstring invoeren en controleren
########################################################
# hier komt het antwoord op opdracht 1

while True:
    bitstring = input("Gelieve een bitstring in te typen:")
    geldig = True
    errors = []
    lengte = len((bitstring))

    # Herhaalt tot de gebruiker "STOP" intypt
    if bitstring == "STOP":
        print("Programma stopt.")
        break

    #a) De lengte van de string is minstens 22 is.
    if lengte < 22:
        geldig = False
        errors.append("De lengte van de string is minstens 22 is.")

    #b) De string bestaat enkel uit de karakters "0" en "1".
    isBinairy = True     #Het voorkomen van meerdere keren Error printen
    for i in bitstring: 
        if i != "0" and i != "1":
            geldig = False
            isBinairy = False 
    if isBinairy == False:
        errors.append("De string bestaat enkel uit de karakters '0' en '1'.")

    
    #c) De lengte van de string verminderd met 8 moet een veelvoud zijn van 14   
    if (lengte - 8) % 14 != 0:
        geldig = False
        errors.append("De lengte van de string verminderd met 8 moet een veelvoud zijn van 14.")

    # Printen 
    if geldig:
        print("Dit is een geldige bitstring!")
    else: 
        print("Dit is GEEN geldige bitstring!")
        for i in errors:
            print(i)
    
a = "aaaaaaaa"