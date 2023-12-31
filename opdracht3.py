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
#%% Opdracht 3. functie berekenIDnummer()
########################################################
# hier komt het antwoord op opdracht 3

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

def berekenIDnummer(bitstring):
    if isGeldig(bitstring):
        bitstring = bitstring[4:-4] 
        
        bitstring = bitstring.replace("11", "b")
        bitstring = bitstring.replace("00", "b")
        bitstring = bitstring.replace("1", "s")
        bitstring = bitstring.replace("0", "s")   
        
        zwartestring = bitstring[::2] #alle b/s'en met even indexen
        wittestring = bitstring[1::2] #alle b/s'en met oneven indexen
        barcode = ""
        getal = "ssbbsbsssbsbssbbbsssssbsbbsbsssbbsssssbbbssbssbsbs"
        for j in range(int(len(zwartestring)/5)):
            for i in range(50):
                if zwartestring[j*5:j*5+5] == getal[i*5:i*5+5]:
                    barcode += str(i)
        
            for i in range(50):
                if wittestring[j*5:j*5+5] == getal[i*5:i*5+5]:
                    barcode += str(i)
      
        return barcode

aankopen = infoFun.listRead("C:\WetenschappelijkProgrammeren\Project\Project-Wetenschappelijk-Programmeren-1/aankopen.txt")
prijslijst = infoFun.listRead("C:\WetenschappelijkProgrammeren\Project\Project-Wetenschappelijk-Programmeren-1/prijslijst.txt")

aankopenlijst = []
totaalprijs = 0
lijst = []

for i in aankopen: 
    ID = berekenIDnummer(i)
    aankopenlijst = aankopenlijst + [ID]

for i in prijslijst: 
    splitsen = i.split()
    lijst.append(splitsen)

for i in range(len(lijst)):
    for j in aankopenlijst:
        if lijst[i][0] == j:
            totaalprijs = totaalprijs + float(lijst[i][1])       
            
print("De totaalprijs is: ", round(totaalprijs, 2))


