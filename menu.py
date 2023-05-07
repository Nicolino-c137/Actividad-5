import sys, os

class Menu:
    __planes= None
    __elecciones= {}
    
    def __init__(self,lista):
        self.__planes= lista
        self.__elecciones= {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.opcion5,
            '0': self.salir
        }
        
    def mostrarMenu(self):
        print("""
MENU PRINCIPAL

1. Actualizar el valor del vehiculo de cada plan
2. Mostrar plan adecuado a su importe
3. Mostrar monto a pagar para licitar un vehículo
4. Modificar cantidad de cuotas a pagar para licitar un vehículo
5. Modificar cantidad de cuotas del plan
0. Salir
""")
        
    def generarMenu(self):
        while True:
            self.mostrarMenu()
            op= input("Seleccion alguna opción: ")
            os.system("cls")
            ejecutar= self.__elecciones.get(op)
            if ejecutar:
                ejecutar()
            else: 
                print("Opcion no valida, vuelva a intentarlo")
                os.system("pause")
            
            
    def opcion1(self):
        print("1. Actualizar el valor del vehiculo de cada plan")
        print()
        for plan in self.__planes:
            plan.actualizarValor()
        os.system("pause")
           
    def opcion2(self):
        print("2. Mostrar plan adecuado a su importe")
        print()
        resultado= 0
        valor= float(input("Ingrese un importe para ver los planes mas adecuados a usted: "))
        for plan in self.__planes:
            resultado+= plan.verDatos(valor)
        if resultado == len(self.__planes):
            print("No hay ningun tipo de plan disponible")
        os.system("pause")
    
    def opcion3(self):
        print("3. Mostrar monto que se debe pagar para licitar un vehículo")
        print()
        for plan in self.__planes:
            print(f"Para el plan {plan.getCodigo()} se necesita un monto de ${plan.mostrarMonto_paraLicitar():.2f} para licitar un vehículo")
        os.system("pause")
    
    def opcion4(self):
        print("4. Modificar cantidad de cuotas a pagar para licitar un vehículo")
        print()
        cod= int(input("Ingrese el codigo de un plan para modificar la cantidad de cuotas: "))
        bandera= False
        i=0
        while not bandera and i < len(self.__planes):
            if self.__planes[i].getCodigo() == cod:
                self.__planes[i].modificarCuotas_paraLicitar()
                bandera= True
            else: i+=1
        if i == len(self.__planes):
            print("No se encontró el codigo de plan ingresado")
        os.system("pause")
        
    def opcion5(self):
        print("5. Modificar cantidad de cuotas del plan")
        print()
        cod= int(input("Ingrese el codigo de un plan para modificar la cantidad de cuotas: "))
        bandera= False
        i=0
        while not bandera and i < len(self.__planes):
            if self.__planes[i].getCodigo() == cod:
                self.__planes[i].modificarCuotas()
                bandera= True
            else: i+=1
        if i == len(self.__planes):
            print("No se encontró el codigo de plan ingresado")
        os.system("pause")
    
    def salir(self):
        sys.exit(0)