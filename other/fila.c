#include <stdio.h>
#include <stdlib.h>

typedef struct cel {
  int value;
  struct cel *next;
} cel;

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

void remove_cell(cel *p) {
  cel *d = p->next;
  p->next = d->next;
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
    p = add_cell(p, i, 2);
  }
 return 0;
}