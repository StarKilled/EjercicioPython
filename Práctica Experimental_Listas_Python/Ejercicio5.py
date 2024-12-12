# Función que calcula el factorial de un número n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
n = int(input("Ingresa el número para calcular su factorial: "))
print(f"El factorial de {n} es: {factorial(n)}")
