#include <stdio.h>
#include <stdlib.h>

typedef struct veia
{
  char nome;
  int idade;
};

typedef struct cel {
  veia value;
  struct cel *next;
} cel;

// sem cabeça

cel *add_veia_na_fila(cel *p, veia valor) {
  cel *new_p = (cel *)malloc(sizeof(cel));
  new_p->value = valor;

  new_p->next = p;
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
  veia veia1 = {'a', 1};
  veia veia2 = {'b', 2};
  veia veia3 = {'c', 3};
  veia veia4 = {'d', 4};
  veia veia5 = {'e', 5};

  celula->value = veia1;

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