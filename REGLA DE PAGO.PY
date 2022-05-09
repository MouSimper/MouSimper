# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:05:06 2022

@author: USUARIO
"""
def main():
    x=float(input("Ingresar dinero en efectivo: "))
    if x<=100:
        print("Pagar con dinero en efectivo")
    elif x>100 and x<=300:
        print("Pagar con tarjeta de débito")
    else:
        print("Pago con tarjeta de crédito")
main()