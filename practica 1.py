print() #para dejar un espacio al momento de ejcutar 
print("jose daniel arguijo torres")
print() #para dejar un espacio al momento de ejecutar 

class Alumno:
    def __init__(self, nombre, nota):
        
        self.nombre = nombre
        self.nota = nota

    def imprimir_info(self):
        
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        
        if self.nota >= 5:
            print(f"El alumno {self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"El alumno {self.nombre} no ha aprobado. Nota: {self.nota}.")

alumno1 = Alumno("jose daniel", 7)

alumno1.imprimir_info()

alumno1.resultado()
