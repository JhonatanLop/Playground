#include <stdio.h>
#include <stdlib.h>

typedef struct cel {
  int value;
  struct cel *next;
} cel;


cel *add_cell(cel *p, int valor) {
  cel *new_p = (cel *)malloc(sizeof(cel));

  new_p->value = valor;

  // insere_topo
  new_p->next = p;
  return new_p;
}

remove_cel(cel *p) {
  *p = *p->next;
}

void print(cel *p) {
  cel *aux = p;
  while (aux->next != NULL) {
    printf("%d\n", aux->value);
    aux = aux->next;
  }
  printf("%d\n", aux->value);
  printf("\n");
}

int main(int argc, char const *argv[])
{
  cel *pilha = (cel *)malloc(sizeof(cel));
  pilha->value = 1;
  pilha->next = NULL;

  pilha = add_cell(pilha, 2);
  pilha = add_cell(pilha, 3);
  pilha = add_cell(pilha, 4);
  pilha = add_cell(pilha, 5);

  print(pilha);

  remove_cel(pilha);
  remove_cel(pilha);

  print(pilha);

  return 0;
}
