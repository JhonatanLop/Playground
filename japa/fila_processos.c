#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct cel {
  int algoritmo;
  struct cel *next;
} cel;


// insere pessoa na fila
void inserir_comando(int command, cel**init, cel**fim){
  cel *new = (cel*)malloc(sizeof(cel));
  new->algoritmo = command;
  new->next = NULL;

  if (*init == NULL) {
    *init = new;
    *fim = new;
  } else {
    (*fim) = new;
    *fim = new;
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
void print(cel*fim){

  cel *act = fim->next;
  while (act->next != NULL)
  {
    printf("\n%c", act->algoritmo);
    act = act->next;
  }
  printf("\n%c", act->algoritmo);
}

// função que testa o algoritmo
int main(){

  int c1 = 'a';
  int c2 = 'b';
  int c3 = 'c';
  int c4 = 'd';
  int c5 = 'e';

  cel **init = NULL;
  cel **fim = NULL;

  inserir_comando(c1, init, fim);
  printf("Comando: %c\n", fim);
  inserir_comando(c2, init, fim);
  inserir_comando(c3, init, fim);
  inserir_comando(c4, init, fim);
  inserir_comando(c5, init, fim);
  // print(fim);


  // int comando = extrair_comando(fim);
  // printf("\nComando extraido: %c\n", comando);

  // int comandoa = extrair_comando(fim);
  // printf("\nComando extraido: %c\n", comandoa);

  // print(fim);

  // printf("\nInserindo comando 'f'\n");
  // int c6 = 'f';
  // inserir_comando(c6, init, fim);

  // print(fim);

  return 0;
}