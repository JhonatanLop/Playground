/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

typedef struct cel {
  int value;
  struct cel *next;
} cel;

void swap(cel *p, cel *q) {
  cel temp = *p;
  *p = *q;
  *q = temp;
}

int list_lengh(cel *p) {
  int cont = 0;
  while (p->next != NULL) {
    cont += 1;
    p = p->next;
  }
  return cont;
}

void sort(cel *p, int size) {
  int count = 1;
  for (size_t i = 0; i < (size - 1); i++) {
    cel *head = (p + i + 1);
    while (head->next != NULL) {
      if ((p + i)->value > head->value) {
        swap((p + i), (p + count));
        continue;
      }
      count++;
      head = head->next;
    }
  }
}

cel *add_cell(cel *p, int valor, int posicao) {
  cel *new_p = (cel *)malloc(sizeof(cel));

  new_p->value = valor;

  // insere antes
  if (posicao == 1) {
    new_p->next = p;
    return new_p;
  }
  // insere depois
  else {
    new_p->next = p->next;
    p->next = new_p;
    return p;
  }
}

void print(cel *p) {
  cel *head = p;
  while (head->next != NULL) {
    printf("%d ", head->value);
    head = head->next;
  }
}

int main()
{
  int count;
  cel *celula = (cel *)malloc(sizeof(cel));

  celula->value = 69;
  celula->next = NULL;

  // criando fila
  for (int i = 0; i < 4; i++) {
    cel *p = celula;
    p = add_cell(p, i, 2);

    int size = list_lengh(p);
    sort(p, size);

    if (i == 3) {
      print(p);
    }
  }
 return 0;
}
