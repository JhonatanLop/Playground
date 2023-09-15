#include <stdio.h>

// Protótipo da função
void trocarValores(int *A, int *B);

int main(void) {
  int A = 5;
  int B = 10;

  trocarValores(&A, &B);

  printf("A = %i\n", A);
  printf("B = %i\n", B);
  return 0;
}

void trocarValores(int *A, int *B) {
  int temp = *A;
  *A = *B;
  *B = temp;
}