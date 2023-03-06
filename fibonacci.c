#include <stdio.h>

int main() {
    int num, ant1 = 0, ant2 = 1, fib = 0, encontrado = 0;

    printf("Informe um número: ");
    scanf("%d", &num);

    while (fib <= num) {
        if (fib == num) {
            encontrado = 1;
            break;
        }
        fib = ant1 + ant2;
        ant1 = ant2;
        ant2 = fib;
    }

    if (encontrado) {
        printf("%d pertence à sequência de Fibonacci.", num);
    } else {
        printf("%d não pertence à sequência de Fibonacci.", num);
    }

    return 0;
}
