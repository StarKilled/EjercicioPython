#include <stdio.h>

int main() {
    char respuesta;

    do {
        // Imprimir "Hola, Mundo"
        printf("Hola, Mundo\n");

        // Preguntar al usuario si quiere repetir
        printf("¿Quieres ver 'Hola, Mundo' de nuevo? (s/n): ");
        scanf(" %c", &respuesta);

    } while (respuesta == 's' || respuesta == 'S'); // Repite si la respuesta es 's' o 'S'

    return 0;
}
