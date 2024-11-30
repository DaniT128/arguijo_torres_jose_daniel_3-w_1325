print() #para dejar un espacio al momento de ejcutar 
print("jose daniel arguijo torres")
print() #para dejar un espacio al momento de ejecutar 

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        
        lado_mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con el tamaño mayor es: {lado_mayor}")

    def tipo_triangulo(self):
        
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

triangulo1 = Triangulo(5, 5, 8)

triangulo1.imprimir_lado_mayor()

triangulo1.tipo_triangulo()

triangulo2 = Triangulo(6, 6, 6)

triangulo2.imprimir_lado_mayor()

triangulo2.tipo_triangulo()

triangulo3 = Triangulo(4, 5, 6)

triangulo3.imprimir_lado_mayor()

triangulo3.tipo_triangulo()
