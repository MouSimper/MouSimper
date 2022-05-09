# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:18:19 2022

@author: USUARIO
"""

def main():
    x=float(input("Ingrese el año actual: "))
    y=float(input("Ingrese cualquier año: "))
    z=x-y
    if x<z:
        print("Han pasado",z,"años")
    elif x>z:
        print("Faltan",z*-1,"años")
    else:
        print("Es el año actual")
main()