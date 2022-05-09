# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:18:04 2022

@author: USUARIO
"""
def main():
    Monto=float(input("Ingrese el monto: "))
    Tasa=0.004074
    Mes=Monto*(1+Tasa)
    Mes1=(Monto+Mes)*(1+Tasa)
    Mes2=(Monto+Mes1)*(1+Tasa)
    Mes3=(Monto+Mes2)*(1+Tasa)
    print("El valor al 2to Mes es",Mes1)
    print("El valor al 3to Mes es",Mes2)
    print("El valor al 4to Mes es",Mes3)
main()
    