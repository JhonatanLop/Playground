#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_NAME_LENGTH 100

typedef struct cel {
  char algoritmo;
  struct cel *next;
} cel;

typedef struct fila {
  cel *inicio;
  cel *fim;
} fila;

fila create_empty_fila(){
  fila f;
  f.inicio = NULL;
  f.fim = NULL;
  return f;
}

// insere pessoa na fila
void inserir_comando(char comando, fila *f){
  cel *new = (cel *)malloc(sizeof(cel));
  new->algoritmo = comando;
  new->next = NULL;
  if(f->inicio == NULL)
  {
    f->inicio = new;
    f->fim = new;
  }
  else
  {
    f->fim->next = new;
    f->fim = new;
  }
}

char extrair_comando(fila *f){
  if (f->inicio == NULL){
    printf("Fila vazia");
    exit(1);
  } else{
    cel *p = f->inicio;
    f->inicio = f->inicio->next;
    char command = p->algoritmo;
    free(p);
    return command;
  }
}

// imprime a fila
void print(fila *f){
  cel *aux = f->inicio;
  while (aux->next != NULL) {
    printf("%c\n", aux->algoritmo);
    aux = aux->next;
  }
  printf("%c\n", aux->algoritmo);
}

// função que testa o algoritmo
int main(){
  fila f = create_empty_fila();
  char c1 = 'a';
  char c2 = 'b';
  char c3 = 'c';
  char c4 = 'd';
  char c5 = 'e';

  inserir_comando(c1, &f);
  inserir_comando(c2, &f);
  inserir_comando(c3, &f);
  inserir_comando(c4, &f);
  inserir_comando(c5, &f);

  print(&f);

  char comando = extrair_comando(&f);
  printf("\nComando extraido: %c\n", comando);

  char comandoa = extrair_comando(&f);
  printf("\nComando extraido: %c\n", comandoa);

  print(&f);

  printf("\nInserindo comando 'f'\n");
  char c6 = 'f';
  inserir_comando(c6, &f);

  print(&f);

  return 0;
}