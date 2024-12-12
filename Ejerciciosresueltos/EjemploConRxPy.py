from rx import create
from rx.operators import map, filter

# Función para crear un observable
def observable_example(observer, _):
    for i in range(10):
        observer.on_next(i)  # Envía un dato al flujo
    observer.on_completed()  # Indica que se completó el flujo

# Crear el flujo
observable = create(observable_example)

# Suscripción al observable con transformaciones
observable.pipe(
    filter(lambda x: x % 2 == 0),  # Filtrar números pares
    map(lambda x: x * 2)          # Multiplicar cada número por 2
).subscribe(
    on_next=lambda x: print(f"Received: {x}"),  # Acciones para cada dato
    on_error=lambda e: print(f"Error: {e}"),
    on_completed=lambda: print("Completed!")
)