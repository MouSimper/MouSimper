# -*- coding: utf-8 -*-
"""
Created on Mon May  9 12:43:37 2022

@author: USUARIO
"""

def main():
    subtotal=float(input("Ingrese el subtotal: "))
    tasa=float(input("Ingrese la tasa de gratuidad: "))
    total=subtotal*tasa
    print("El tasa de gratuidad es:",tasa,"y el total es",total)
main()