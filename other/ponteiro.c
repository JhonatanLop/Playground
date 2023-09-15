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


int A = 10; // 0x200
int B = 20; // 2x300

int *PA; // 3x100 - declaração de ponteiro
int *PB; // 5x230

PA = NULL; // sempre coloque null
PB = NULL;

PA = &A; // PA aponta para endereço de memória de A
PB = &B; // PB aponta para endereço de memória de B

printf ("%d", *PB); // tela: 20    aponta valor de PB
printf ("%d", PB); // tela: 2x300  aponta endereço de B
printf ("%d", &PB); // tela: 5x230 aponta endereço de PB

A = *PA * (*PB); // A * B

void Sub (int *a, int *b){
    *a = *a - *b;
    *b = *b++;
}