#include <stdio.h>

int main() {
    printf("prueba");
    printf("\n");
    int n, e = 0;
    printf("Número de elementos: ");
    scanf("%d", &n);
    
    int arr[n];
    
    printf("Ingrese el valor de los elementos:\n");
    do {
        scanf("%d", &arr[e]);
        e++;
    } while (e < n);


    //pares
    printf("Pares: ");
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            printf("%d ", arr[i]);
        }
    }
    printf("\n"); 

    //impares
    printf("Impares: ");
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) {
            printf("%d ", arr[i]);
        }
    }
    printf("\n");

    return 0;
}

