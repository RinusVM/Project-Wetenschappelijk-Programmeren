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
#%% Opdracht 3. functie berekenIDnummer()
########################################################
# hier komt het antwoord op opdracht 5

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


def berekenIDnummer(bitstring):
    if isGeldig(bitstring):
        bitstring = bitstring[4:-4] 
        
        bitstring = bitstring.replace("11", "b")
        bitstring = bitstring.replace("00", "b")
        bitstring = bitstring.replace("1", "s")
        bitstring = bitstring.replace("0", "s")   
        
        zwartestring = bitstring[::2] #alle b/s'en met even indexen
        wittestring = bitstring[1::2] #alle b/s'en met oneven indexen
        
        getal = "ssbbsbsssbsbssbbbsssssbsbbsbsssbbsssssbbbssbssbsbs"
        for i in range(0, len(getal)):
            if zwartestring == getal[i*5:i*5+5]:
                kar1 = i
        
        for i in range(0,len(getal)-4):
            if wittestring == getal[i*5:i*5+5]:
                kar2 = i
      
        ID = str(kar1) + str(kar2)
        return ID

# test code
ID = berekenIDnummer("1010110100100101101101")
print(ID) # '16'

barcode1 = "1010110101001101001011010010011011001010101100100110101011001011010110010010100101101100101010011001101101"
barcode2 = "1010110100101011001010011001011010110010100110101101011001001100110101001011001011001010110101101001001101"
barcode3 = "1010110011010010101001101010011010110110010010101101001001101100101011010011010010010110100110101011001101"
#ID1 = berekenIDnummer(barcode1) # '84201121977270'
#ID2 = berekenIDnummer(barcode2) # '12462997385557'
#ID3 = berekenIDnummer(barcode3) # '35286020811621'

