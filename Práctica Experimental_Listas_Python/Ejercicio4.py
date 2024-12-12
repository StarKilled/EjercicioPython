# Función que devuelve la serie de Fibonacci hasta el n-ésimo término
def fibonacci(n):
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie

# Ejemplo de uso
n = int(input("Ingresa el número de términos de Fibonacci que deseas: "))
print(f"La serie de Fibonacci hasta el término{n} es: {fibonacci(n)}")
