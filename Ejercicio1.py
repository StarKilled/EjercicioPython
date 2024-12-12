import math

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass

    def mostrar_info(self):
        print(f"Nombre de la figura: {self.nombre}")


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Base: {self.base}, Altura: {self.altura}")
        print(f"Área: {self.area()}, Perímetro: {self.perimetro()}")


class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado1 + self.lado2

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Base: {self.base}, Altura: {self.altura}")
        print(f"Lado 1: {self.lado1}, Lado 2: {self.lado2}")
        print(f"Área: {self.area()}, Perímetro: {self.perimetro()}")


class Hexagono(Figura):
    def __init__(self, lado):
        super().__init__("Hexágono")
        self.lado = lado

    def area(self):
        return (3 * math.sqrt(3) / 2) * (self.lado ** 2)

    def perimetro(self):
        return 6 * self.lado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Lado: {self.lado}")
        print(f"Área: {self.area():.2f}, Perímetro: {self.perimetro()}")


class MenuFiguras:
    def __init__(self):
        self.figuras = []

    def agregar_rectangulo(self, base, altura):
        rectangulo = Rectangulo(base, altura)
        self.figuras.append(rectangulo)

    def agregar_triangulo(self, base, altura, lado1, lado2):
        triangulo = Triangulo(base, altura, lado1, lado2)
        self.figuras.append(triangulo)

    def agregar_hexagono(self, lado):
        hexagono = Hexagono(lado)
        self.figuras.append(hexagono)

    def mostrar_figuras(self):
        for figura in self.figuras:
            figura.mostrar_info()
            print('-' * 30)

    def menu(self):
        while True:
            print("\nMenu de Figuras:")
            print("1. Agregar Rectángulo")
            print("2. Agregar Triángulo")
            print("3. Agregar Hexágono")
            print("4. Mostrar Figuras")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                self.agregar_rectangulo(base, altura)
            elif opcion == "2":
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                lado1 = float(input("Ingrese el lado 1 del triángulo: "))
                lado2 = float(input("Ingrese el lado 2 del triángulo: "))
                self.agregar_triangulo(base, altura, lado1, lado2)
            elif opcion == "3":
                lado = float(input("Ingrese el lado del hexágono: "))
                self.agregar_hexagono(lado)
            elif opcion == "4":
                self.mostrar_figuras()
            elif opcion == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu = MenuFiguras()
    menu.menu()
