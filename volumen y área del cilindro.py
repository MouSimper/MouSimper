# -*- coding: utf-8 -*-
"""
Created on Mon May  9 12:39:55 2022

@author: USUARIO
"""

def main():
    x=float(input("Ingrese la longitud del cilindro: "))
    y=float(input("Ingrese el radio del cilindro: "))
    pi=3.14159
    área=x*y*pi
    volumen=área*x
    print("El área del cilindro es:",área)
    print("El volumen del cilindro es:", volumen)
main()
    