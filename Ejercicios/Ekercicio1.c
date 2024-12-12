#include <stdio.h>

int main() {
    int lim = 12;
    int num;
    printf("Introduce un número: ");
    scanf("%d", &num);
    
    for (int i = 1; i <= lim; i++) {
        int resultado = num * i;
        printf("%d x %d = %d\n", num, i, resultado);
    }

    int sum = 0;
    int i = 0;
    int nums[] = {2, 4, 5, 10, 8, 15, 20, 19, 23, 48, 70, 45, 30};
    int size = sizeof(nums) / sizeof(nums[0]);

    while (i < size) {
        if (nums[i] % 2 == 0) {
            sum = sum + 1;
        }
        i++;
    }
    printf("Hay %d números pares\n", sum);

    return 0;
}
