def encontrar_mayor(lista):
    if len(lista) == 0:
        return None  # Manejo de lista vacía
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

# Prueba de la función
numeros = [10, 24, 56, 7, 34]
print(f"El mayor número es: {encontrar_mayor(numeros)}")

