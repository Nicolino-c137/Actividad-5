class Plan_Ahorro:
    __codigo_plan: int
    __modelo_vehiculo= str
    __version_vehiculo= str
    __valor_vehiculo= float
    __cuotas_plan= 60
    __cuotas_a_tener_pagas= 10
    
    def __init__(self,codigo=None,modelo=None,version=None,valor=None):
        self.__codigo_plan= codigo
        self.__modelo_vehiculo= modelo
        self.__version_vehiculo= version
        self.__valor_vehiculo= valor
        
    def getCodigo(self):
        return int(self.__codigo_plan)
    
    def getModelo(self):
        return self.__modelo_vehiculo
    
    def getVersion(self):
        return self.__version_vehiculo
    
    def actualizarValor(self):
        print(f"""
Actualizar valor del vehículo:
Código del plan: {self.getCodigo()}
Modelo del vehículo: {self.getModelo()}
Versión del vehículo: {self.getVersion()}
""")
        nuevo_valor= float(int(input("Ingrese el nuevo valor del vehículo: ")))
        self.__valor_vehiculo= nuevo_valor
        print("Valor modificado con éxito!")
    
    def get_importeCuota(self):
        importe= (float(self.__valor_vehiculo)/self.__cuotas_plan) + float(self.__valor_vehiculo) * 0.10
        return importe
    
    def verDatos(self,valor):
        if float(self.get_importeCuota()) <valor:
            print(f"""
Código del plan: {self.getCodigo()}
Modelo del vehículo: {self.getModelo()}
Versión del vehículo: {self.getVersion()}""")
        else: return 1
                   
    def mostrarMonto_paraLicitar(self):
        return self.__cuotas_a_tener_pagas * self.get_importeCuota()
    
    #Metodos de clase
    @classmethod
    def modificarCuotas_paraLicitar(cls):
        nueva_cantidad= int(input("Ingrese la nueva cantidad de cuotas que se debe tener pagadas para licitar el vehículo: "))
        cls.__cuotas_a_tener_pagas= nueva_cantidad
        print("Cuotas modificadas con éxito!")
        
    @classmethod
    def modificarCuotas(cls):
        nueva_cant= int(input("Ingrese la nueva cantidad de cuotas que debe tener el plan: "))
        cls.__cuotas_plan= nueva_cant
        print("Cuotas modificadas con éxito!")