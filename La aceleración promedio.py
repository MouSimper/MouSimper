# -*- coding: utf-8 -*-
"""
Created on Mon May  9 12:48:57 2022

@author: USUARIO
"""

def main():
    Vi=float(input("Ingrese la velocidad inicial: "))
    Vf=float(input("Ingrese la velocidad final: "))
    T=float(input("Ingrese el tiempo: "))
    A=(Vf-Vi)/T
    print("La aceleración es:",A)
main()