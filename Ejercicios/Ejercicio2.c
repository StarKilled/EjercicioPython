#include <stdio.h>
#define M_PI 3.141592653589793  // Definimos el valor de PI manualmente

// Función para calcular el área de un triángulo
float areaTriangulo(float base, float altura) {
    return (base * altura) / 2;
}

// Función para calcular el área de un cuadrado
float areaCuadrado(float lado) {
    return lado * lado;
}

// Función para calcular el área de un cilindro
float areaCilindro(float radio, float altura) {
    return 2 * M_PI * radio * (radio + altura);
}

// Función para calcular el área de un círculo
float areaCirculo(float radio) {
    return M_PI * radio * radio;
}

// Función para calcular el área de un rombo
float areaRombo(float diagonalMayor, float diagonalMenor) {
    return (diagonalMayor * diagonalMenor) / 2;
}

int main() {
    int opcion;
    float base, altura, lado, radio, diagonalMayor, diagonalMenor;
    
    printf("Seleccione la figura para calcular su área:\n");
    printf("1. Triángulo\n");
    printf("2. Cuadrado\n");
    printf("3. Cilindro\n");
    printf("4. Círculo\n");
    printf("5. Rombo\n");
    printf("Opción: ");
    scanf("%d", &opcion);
    
    switch (opcion) {
        case 1:
            printf("Ingrese la base del triángulo: ");
            scanf("%f", &base);
            printf("Ingrese la altura del triángulo: ");
            scanf("%f", &altura);
            printf("El área del triángulo es: %.2f\n", areaTriangulo(base, altura));
            break;
        case 2:
            printf("Ingrese el lado del cuadrado: ");
            scanf("%f", &lado);
            printf("El área del cuadrado es: %.2f\n", areaCuadrado(lado));
            break;
        case 3:
            printf("Ingrese el radio del cilindro: ");
            scanf("%f", &radio);
            printf("Ingrese la altura del cilindro: ");
            scanf("%f", &altura);
            printf("El área del cilindro es: %.2f\n", areaCilindro(radio, altura));
            break;
        case 4:
            printf("Ingrese el radio del círculo: ");
            scanf("%f", &radio);
            printf("El área del círculo es: %.2f\n", areaCirculo(radio));
            break;
        case 5:
            printf("Ingrese la diagonal mayor del rombo: ");
            scanf("%f", &diagonalMayor);
            printf("Ingrese la diagonal menor del rombo: ");
            scanf("%f", &diagonalMenor);
            printf("El área del rombo es: %.2f\n", areaRombo(diagonalMayor, diagonalMenor));
            break;
        default:
            printf("Opción no válida.\n");
            break;
    }
    
    return 0;
}
