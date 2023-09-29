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

cel* add_cell(cel *p, int valor, int posicao) {
  cel *new_p = (cel *)malloc(sizeof(cel));
  // insere antes
  if (posicao == 1){
    new_p->value = valor;
    new_p->next = p;
    return new_p;
  }
  // insere depois
  else {
    new_p->next = p->next;
    new_p->value = valor;
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
    printf("salve\nesse é meu algoritmo pra manipulação de celulas");

    printf("Criando célula");
    cel celula = create_cell(69);
    printf("adicionando célula");
    cel * myCell;
    myCell = &celula;
    myCell = (myCell,96,1);
    
    printf("");
}