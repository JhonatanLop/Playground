#include <stdio.h>
#include <stdlib.h>

typedef struct cel {
  int value;
  struct cel *next;
} cel;

cel *add_cell_fila(cel *p, int valor) {
    cel *head = p;
  cel *new_p = (cel *)malloc(sizeof(cel));

  new_p->value = valor;

  // insere antes
    new_p->next = head;
    return new_p;
}

void remove_cell(cel *p) {
  cel *d = p;
  while (d->next->next != NULL)
  {
    d = d->next;
  }
  d->next = NULL;
}

void print(cel *p) {
  cel *head = p;
  while (head->next != NULL) {
    printf("%d ", head->value);
    head = head->next;
  }
  printf("%d ", head->value);
}

int main() {
  int count;
  cel *celula = (cel *)malloc(sizeof(cel));

  celula->value = 0;
  celula->next = NULL;

  celula = add_cell_fila(celula, 1);
  celula = add_cell_fila(celula, 2);
  celula = add_cell_fila(celula, 3);
  celula = add_cell_fila(celula, 4);
  celula = add_cell_fila(celula, 5);

  remove_cell(celula);
  remove_cell(celula);

 print(celula);  // 5 4 3 2 1
  
 return 0;
}