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
  free(d);
}

int main() {
  int count;
  cel *celula = (cel *)malloc(sizeof(cel));

  celula->value = 69;
  celula->next = NULL;

  // criando fila
  for (int i = 0; i < 4; i++) {
    cel *p = celula;
    p = add_cell(p, i);
  }
 return 0;
}