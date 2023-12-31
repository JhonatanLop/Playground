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

int list_lengh(cel *p) {
  int cont = 0;
  while (p->next != NULL) {
    cont += 1;
    p = p->next;
  }
  return cont;
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

  // criando fila
  for (int i = 0; i < 4; i++) {
    cel *p = celula;
    p = add_cell(p, i, 2);

    if (i == 3) {
      print(p);
    }
  }
 return 0;
}