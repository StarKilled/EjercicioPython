# Ejemplo de uso de listas en Python

# Creación de una lista
mi_lista = [10, 20, 30, 40, 50]
print("Lista inicial:", mi_lista)

# Acceso a elementos de la lista
print("Primer elemento:", mi_lista[0])
print("Último elemento:", mi_lista[-1])

# Modificar un elemento de la lista
mi_lista[2] = 35
print("Lista después de modificar el tercer elemento:", mi_lista)

# Agregar elementos a la lista
mi_lista.append(60)
print("Lista después de agregar un elemento al final:", mi_lista)

# Insertar un elemento en una posición específica
mi_lista.insert(1, 15)
print("Lista después de insertar un elemento en la posición 1:", mi_lista)

# Eliminar un elemento de la lista
mi_lista.remove(40)
print("Lista después de eliminar el elemento 40:", mi_lista)

# Eliminar un elemento por su índice
eliminado = mi_lista.pop(2)
print(f"Elemento eliminado en la posición 2: {eliminado}")
print("Lista después de usar pop:", mi_lista)

# Encontrar el índice de un elemento
indice = mi_lista.index(50)
print("Índice del elemento 50:", indice)

# Contar cuántas veces aparece un elemento
conteo = mi_lista.count(20)
print("Número de veces que aparece 20:", conteo)

# Ordenar la lista
mi_lista.sort()
print("Lista ordenada:", mi_lista)

# Revertir la lista
mi_lista.reverse()
print("Lista en orden inverso:", mi_lista)

# Copiar la lista
copia_lista = mi_lista.copy()
print("Copia de la lista:", copia_lista)

# Vaciar la lista
mi_lista.clear()
print("Lista después de vaciarla:", mi_lista)

# Trabajar con listas anidadas
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Lista anidada:", lista_anidada)
print("Elemento [1][2] de la lista anidada:", lista_anidada[1][2])

# Uso de listas por comprensión
cuadrados = [x**2 for x in range(10)]
print("Lista de cuadrados usando comprensión de listas:", cuadrados)

# Verificar si un elemento está en la lista
print("¿Está 50 en la lista de copia?", 50 in copia_lista)
print("¿Está 100 en la lista de copia?", 100 in copia_lista)
