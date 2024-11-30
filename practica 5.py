print()
print("jose daniel arguijo torres")
print()

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        print("Contacto añadido.")

    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos.")
        else:
            for c in self.contactos:
                print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}")

    def buscar_contacto(self):
        nombre = input("Nombre a buscar: ")
        for c in self.contactos:
            if c["nombre"].lower() == nombre.lower():
                print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}")
                return
        print("Contacto no encontrado.")

    def editar_contacto(self):
        nombre = input("Nombre a editar: ")
        for c in self.contactos:
            if c["nombre"].lower() == nombre.lower():
                c["nombre"] = input("Nuevo nombre: ") or c["nombre"]
                c["telefono"] = input("Nuevo teléfono: ") or c["telefono"]
                c["email"] = input("Nuevo email: ") or c["email"]
                print("Contacto actualizado.")
                return
        print("Contacto no encontrado.")

    def cerrar_agenda(self):
        print("Agenda cerrada.")
        exit()

    def mostrar_menu(self):
        opciones = {
            "1": self.añadir_contacto,
            "2": self.listar_contactos,
            "3": self.buscar_contacto,
            "4": self.editar_contacto,
            "5": self.cerrar_agenda
        }
        while True:
            print("\n1. Añadir contacto\n2. Listar contactos\n3. Buscar contacto\n4. Editar contacto\n5. Cerrar agenda")
            opcion = input("Elige una opción: ")
            if opcion in opciones:
                opciones[opcion]()
            else:
                print("Opción inválida.")

# Ejecución de la agenda
agenda = Agenda()
agenda.mostrar_menu()


