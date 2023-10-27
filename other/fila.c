#include <stdio.h>
#include <stdlib.h>

typedef struct cel {
  int value;
  struct cel *next;
} cel;

cel *add_cell_fila(cel *p, int valor) {
  cel *new_p = (cel *)malloc(sizeof(cel));

  new_p->value = valor;

  // insere antes
    new_p->next = p;
    return new_p;
}

void remove_cell(cel *p) {
  cel *d = p->next;
  while (d->next->next != NULL)
  {
    d->next = d->next->next;
  }
  d->next = NULL;
  free(d->next);
}

void print(cel *p) {
  cel *head = p;
  while (head->next != NULL) {
    printf("%d ", head->value);
    head = head->next;
  }
}

int main() {
  int count;
  cel *celula = (cel *)malloc(sizeof(cel));

  celula->value = 69;
  celula->next = NULL;

  celula = add_cell_fila(celula, 1);
  celula = add_cell_fila(celula, 2);
  celula = add_cell_fila(celula, 3);
  celula = add_cell_fila(celula, 4);
  celula = add_cell_fila(celula, 5);
  
  printf("%d\n",celula->value);
  printf("%d\n",celula->next->value);
  printf("%d\n",celula->next->next->value);
  printf("%d\n",celula->next->next->next->value);
  printf("%d\n",celula->next->next->next->next->value);
  printf("%d\n",celula->next->next->next->next->next->value);
  
  remove_cell(celula);
  
  printf("%d\n",celula->value);
  printf("%d\n",celula->next->value);
  printf("%d\n",celula->next->next->value); // some a partir daqui
  printf("%d\n",celula->next->next->next->value);
  printf("%d\n",celula->next->next->next->next->value);
  printf("%d\n",celula->next->next->next->next->next->value);
 return 0;
}