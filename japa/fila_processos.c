#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_NAME_LENGTH 100

typedef struct cel {
  char algoritmo;
  struct cel *next;
} cel;

// insere pessoa na fila
void inserir_comando(char comando, cel *init, cel *fim){
  cel *new = (cel *)malloc(sizeof(cel));
  new->algoritmo = comando;
  new->next = NULL;
  if(fim->next == NULL)
  {
    init->next = new;
    fim->next = new;
  }
  else
  {
    new->next = init;
    init = new;
  }
}

char extrair_comando(cel *fim){
  if (fim->next == NULL){
    printf("Sem comandos na fila\n");
    exit(1);
  } else{
    cel *p = fim->next;
    fim->next = fim->next->next;
    char command = p->algoritmo;
    free(p);
    return command;
  }
}

// imprime a fila
void print(cel *fim){
  cel *aux = fim->next;
  while (aux->next != NULL) {
    printf("%c\n", aux->algoritmo);
    aux = aux->next;
  }
  printf("%c\n", aux->algoritmo);
}

// função que testa o algoritmo
int main(){
  char c1 = 'a';
  char c2 = 'b';
  char c3 = 'c';
  char c4 = 'd';
  char c5 = 'e';

  cel *fim;
  cel *init;
  // fim->next = NULL;
  // init->next = NULL;

  cel *proc1 = (cel *)malloc(sizeof(cel));
  fim = proc1;
  init = proc1;
  proc1->algoritmo = '0';
  proc1->next = NULL;


  inserir_comando(c1, init, fim);
  inserir_comando(c2, init, fim);
  inserir_comando(c3, init, fim);
  inserir_comando(c4, init, fim);
  inserir_comando(c5, init, fim);
  print(fim);


  // char comando = extrair_comando(fim);
  // printf("\nComando extraido: %c\n", comando);

  // char comandoa = extrair_comando(fim);
  // printf("\nComando extraido: %c\n", comandoa);

  print(fim);

  printf("\nInserindo comando 'f'\n");
  char c6 = 'f';
  inserir_comando(c6, init, fim);

  print(fim);

  return 0;
}