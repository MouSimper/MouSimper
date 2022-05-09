# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def main():
    monto= float(input("Ingrese el monto:"))
    if monto <=100:
        print("Pagar con efectivo")
    elif monto>100 and monto <=300:
        print("Pago con débito")
    else:
        print("Pago con crédito")
main()
    
    