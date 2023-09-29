#include <stdio.h>

typedef struct cel {
  int value;
  struct cel *next;
} cel;

cel *create_cell(int valor) {
  // aloca espaço na memporia e aponta cel pra esse endereço
  cel *celula = (cel *)malloc(sizeof(cel));

  celula->value = valor;
  celula->next = NULL;
  return celula;
}

void add_cell(cel *p, int valor, bool posicao) {
  cel *new_p = (cel *)malloc(sizeof(cel));
  if (posicao == true){
    new_p->next = p->next;
    new_p->value = valor;
    p = new_p;
  } else {
    new_p->next = p;
    new_p->value = valor;
    p->next = new_p;
  }
}

void remove_cell(cel *p) {
  cel *new_p = (cel *)malloc(sizeof(cel));
  new_p->next = p->next;
  p->next = new_p;
  new_p->value = valor;
}

int main() {}