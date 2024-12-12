#include <stdio.h>
#include <math.h>

void calcularCuotas(float montoCredito, int numCuotas) {
    float tasaInteres = 0.15; // Tasa de interés anual (15%)
    float interesMensual = tasaInteres / 12; // Tasa de interés mensual
    float cuotaFija;
    float saldoCapital = montoCredito;
    float interesPeriodo, amortizacion, capital;

    // Calcular cuota fija
    cuotaFija = montoCredito * interesMensual * pow(1 + interesMensual, numCuotas) /
                (pow(1 + interesMensual, numCuotas) - 1);

    // Mostrar encabezado de la tabla
    printf("No. Cuota\tCapital\t\tAmortización\tInterés\t\tCuota\n");
    printf("------------------------------------------------------------\n");

    for (int i = 1; i <= numCuotas; i++) {
        // Calcular interés del período
        interesPeriodo = saldoCapital * interesMensual;

        // Calcular amortización
        amortizacion = cuotaFija - interesPeriodo;

        // Calcular capital restante
        saldoCapital -= amortizacion;

        // Mostrar datos en la tabla
        printf("%d\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\n", 
                i, saldoCapital > 0 ? saldoCapital : 0, amortizacion, interesPeriodo, cuotaFija);
    }
}

int main() {
    float montoCredito;
    int numCuotas;

    // Entrada de datos
    printf("Ingrese el monto del crédito: ");
    scanf("%f", &montoCredito);
    printf("Ingrese el número de cuotas: ");
    scanf("%d", &numCuotas);

    // Llamar a la función para calcular y mostrar las cuotas
    calcularCuotas(montoCredito, numCuotas);

    return 0;
}
