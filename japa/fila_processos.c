#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct cel {
  int algoritmo;
  struct cel *next;
} cel;


// insere pessoa na fila
void inserir_comando(int comando, cel **init, cel **fim){
  cel *new = (cel*)malloc(sizeof(cel));
  new->algoritmo = comando;
  new->next = NULL;

  // Se estiver vazia
  if ((*init) == NULL){
    (*init) = new;
    (*fim) = new;
    
  } else{
    new->next = (*fim);
    (*fim) = new;
  }
}

int extrair_comando(cel *init){
  if (init){
    printf("Sem comandos na fila\n");
    exit(1);
  } else{
    cel *p = init->next;
    init->next = init->next->next;
    int command = p->algoritmo;
    free(p);
    return command;
  }
}

//printa a pilha
void print(cel *init){
  cel *p = init;
  while(p != NULL){
    printf("%d\n", p->algoritmo);
    p = p->next;
  }
}

// função que testa o algoritmo
int main(){

  int c1 = 3;
  int c2 = 2;
  int c3 = 7;

  cel *init = NULL;
  cel *fim = NULL;

  inserir_comando(c1, &init, &fim);
  inserir_comando(c2, &init, &fim);
  inserir_comando(c3, &init, &fim);

  print(init);
}