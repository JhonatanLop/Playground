#include <stdio.h>

// Crie um programa que declare um array de inteiros e use um ponteiro para iterar sobre os elementos do array e calcular a soma de todos os valores.

int main(){
  int myArray[] = {1,2,3,4,5,6,7,8,7,5,3,5};
  int *ptrArray = myArray;
  int soma = 0;

  for(int i=0; i < sizeof(myArray); i++){
    soma += *ptrArray;
    ptrArray++;
  }

  printf("A soma dos números é: %i\n",soma);
  return 0;
}