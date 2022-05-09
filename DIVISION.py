# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:50:50 2022

@author: USUARIO
"""

def main():
    dividendo= float(input("Ingrese el dividendo: "))
    divisor= float(input("Ingrese el divisor: "))
    if divisor == 0:
        print("No existe la división entre 0")
    else:
        result=dividendo/divisor
        print("El resultado de la división es: ",result)
        if dividendo%divisor==0:
            print("División exacta")
        else:
            print("División no exacta")

main()
10