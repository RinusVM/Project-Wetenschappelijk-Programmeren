# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:35:18 2015

@author: janV
"""

def listReadValues(fileName):
    """ 
    Function to read numbers from a file, this functions reads the complete file and returns a list of floats (one float per line)

    Parameters
    ----------
    fileName : str
        The path (full path or relative w.r.t. the working directory) 
        of the file to read.
        
    """
    file = open(fileName, mode = 'r', encoding="utf-8")
    # read file and put values as strings in a list
    value_str_list = file.read().splitlines() 
    file.close()
    value_float_list = []         # list to hold the values as floats
    for value_str in value_str_list:
        value_float_list.append(float(value_str))
    return(value_float_list)

def listRead(fileName):
    """ 
    Function to read tekst from a file, this functions reads the complete file and returns a list of strings (one string per line)

    Parameters
    ----------
    fileName : str
        The path (full path or relative w.r.t. the working directory) 
        of the file to read.
        
    """
    name_file = open(fileName, mode = 'r', encoding="utf-8")
    mylist = name_file.read().splitlines() 
    name_file.close()
    return(mylist)
    
def stringRead(fileName):
    """ 
    Function to read tekst from a file, this functions reads the complete file and returns a single string

    Parameters
    ----------
    fileName : str
        The path (full path or relative w.r.t. the working directory) 
        of the file to read.
        
    """
    name_file = open(fileName, mode = 'r', encoding="utf-8")
    mystring = name_file.read().strip()
    name_file.close()
    return(mystring)    
    
def listWrite(fileName, list_of_strings):
    """ 
    Function to write a list of strings to a text file (one line per string)

    Parameters
    ----------
    fileName : str
        The path (full path or relative w.r.t. the working directory) 
        of the file that is created (if it exists, it will be overwritten)
        
    list_of_strings : list
        A list of strings that is written to "fileName"
        
    """
    name_file = open(fileName, mode = 'w', encoding="utf-8")
    name_file.write('\n'.join(list_of_strings))
    name_file.close()
    return(None) 
    
def stringWrite(fileName, mystring):
    name_file = open(fileName, mode = 'w', encoding="utf-8")
    name_file.write(mystring)
    name_file.close()
    return(None)    