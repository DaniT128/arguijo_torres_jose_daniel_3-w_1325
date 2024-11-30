print() #para dejar un espacio al momento de ejcutar 
print("jose daniel arguijo torres")
print() #para dejar un espacio al momento de ejecutar 

class Calculadora:
    def __init__(self, valor1, valor2):
        
        self.valor1 = valor1
        self.valor2 = valor2

    def sumar(self):
        
        return self.valor1 + self.valor2

    def restar(self):
        
        return self.valor1 - self.valor2

    def multiplicar(self):
        
        return self.valor1 * self.valor2

    def dividir(self):
        
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: No se puede dividir entre cero."

valor1 = int(input("Ingrese el primer número entero:"))
valor2 = int(input("Ingrese el segundo")) 
