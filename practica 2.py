print() #para dejar un espacio al momento de ejcutar 
print("jose daniel arguijo torres")
print() #para dejar un espacio al momento de ejecutar 

class Persona:
    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def es_mayor_de_edad(self):
        
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")

persona1 = Persona("omar sosa", 20)

persona1.mostrar_datos()

persona1.es_mayor_de_edad()

persona2 = Persona("oscar alonso", 16)

persona2.mostrar_datos()

persona2.es_mayor_de_edad()
