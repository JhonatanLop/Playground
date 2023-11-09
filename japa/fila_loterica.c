#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_NAME_LENGTH 100

typedef struct pessoa {
  char nome[MAX_NAME_LENGTH];
  int idade;
} pessoa;

typedef struct cel {
  pessoa value;
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
void entrar_fila(pessoa senhora, fila *f){
  cel *new = (cel *)malloc(sizeof(cel));
  new->value = senhora;
  new->next = NULL;
  if(f->inicio == NULL)
  {
    printf("Fila vazia");
    f->inicio = new;
    f->fim = new;
  }
  else
  {
    printf("Fila não vazia");
    f->fim->next = new;
    f->fim = new;
  }
}

pessoa sair_fila(fila *f){
  if (f->inicio == NULL){
    printf("Fila vazia");
    exit(1);
  } else{
    cel *p = f->inicio;
    f->inicio = f->inicio->next;
    pessoa senhora = p->value;
    free(p);
    return senhora;
  }
}

// imprime a fila
void print(fila *f){
  cel *p = f->inicio;
  printf("printando a fila' \n");
  while(p != NULL){
    printf("%s, %d anos\n", p->value.nome, p->value.idade);
    p = p->next;
  }
}

// função que testa o algoritmo
int main(){
  fila f = create_empty_fila();
  pessoa p1;
    strcpy(p1.nome,"jhow");
    p1.idade = 20;
  pessoa p2;
    strcpy(p2.nome,"paulin");
    p2.idade = 30;
  pessoa p3;
    strcpy(p3.nome,"marquito");
    p3.idade = 25;
  
  entrar_fila(p1, &f);
  entrar_fila(p2, &f);
  entrar_fila(p3, &f);

  print(&f);

  pessoa senhora = sair_fila(&f);
  printf("\nPessoa removida: %s, %d anos\n", senhora.nome, senhora.idade);

  print(&f);

  return 0;
}