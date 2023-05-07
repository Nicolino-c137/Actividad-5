from clase_planAhorro import Plan_Ahorro as pa
from menu import Menu as m
import csv

def lectura_Archivo():
    with open ("planes.csv") as archivo:
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            cod= fila[0]
            mod= fila[1]
            vers= fila[2]
            valor= fila[3]
            unPlan= pa(cod,mod,vers,valor)
            lista.append(unPlan)

if __name__ == '__main__':
    lista= []
    lectura_Archivo()
    menu= m(lista)
    menu.generarMenu()
    
    
    
    
    
    