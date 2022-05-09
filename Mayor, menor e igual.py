# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:31:13 2022

@author: USUARIO
"""

def main():
    A=int(input("ingresar 1er número: "))
    B=int(input("ingresar 2do número: "))
    if A==B:
        print("Ambos tiene el mismo valor")
    else:
        if A>B:
            print("El mayor valor es",A,"y el menor valor es",B)
        else:
            print("El mayor valor es",B,"y el menor valor es",A)
main()