#include <stdio.h>

int main(void) {

  int *B;      // Declaração de um ponteiro para int chamado B
  int desc = 3; // Declaração de uma variável int chamada desc e atribuição do valor 3 a ela
  B = &desc;   // Atribuição do endereço de desc ao ponteiro B

  // printando o endereço de "desc"
  printf("Endereço = %x", &desc);
  // printando o endereço de "B"
  printf("\nEndereço = %x", &B);
  // printando o valor do qual o ponteiro está referenciando
  printf("\nValor = %x", *B);
  // printando B
  printf("\nValor = %x", B);
}
