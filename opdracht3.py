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

def berekenIDnummer(bitstring):
    # vul aan
    pass

# test code
ID = berekenIDnummer("1010110100100101101101")
print(ID) # '16'

barcode1 = "1010110101001101001011010010011011001010101100100110101011001011010110010010100101101100101010011001101101"
barcode2 = "1010110100101011001010011001011010110010100110101101011001001100110101001011001011001010110101101001001101"
barcode3 = "1010110011010010101001101010011010110110010010101101001001101100101011010011010010010110100110101011001101"
ID1 = berekenIDnummer(barcode1) # '84201121977270'
ID2 = berekenIDnummer(barcode2) # '12462997385557'
ID3 = berekenIDnummer(barcode3) # '35286020811621'

