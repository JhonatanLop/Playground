#include <stdio.h>
#include <stdlib.h>

//Estrutura principal
typedef struct cel {
  int conteudo;
  struct cel *next;
} cel;

//Insere conteudo na fila
void Inserir(int conteudo, cel **fim, cel **init) {
  cel *new = (cel*)malloc(sizeof(cel));
  new->conteudo = conteudo;
  new->next = NULL;

  //Se estiver vazia
  if (*init == NULL) {
    *init = new;
    *fim = new;
  } else { //Se não estiver vazia
    *fim->next = new;
    *fim = new;
  }
}

//Remover e retornar o primeiro elemento da fila
int Extrair(cel **init) {
  if(init == NULL) {
    printf("Sem conteudos na fila\n");
    exit(1);
  } else {
    int command = (*init)->conteudo;
    cel *p = *init;
    *init = (*init)->next;
    free(p);
    return command;
  }
}

//Imprimir a fila
void PrintLista(cel *init) {
  cel *p = init;
  while(p != NULL) {
    printf("%d->", p->conteudo);
    p = p->next;
  } printf("\n");
}

//Liberar a memória
void LiberarLista(cel **init) {
  while(init != NULL) {
    cel *p = *init;
    *init = (*init)->next;
    free(p);
  }
}

//Função principal
int main(void) {
  cel *init = NULL;
  cel *fim = NULL;

  Inserir(3);
  Inserir(2);
  Inserir(7);
  Inserir(2);
  Inserir(3);
  Inserir(5);
  Inserir(9);
  Inserir(8);
  Inserir(2);

  PrintLista();

  Extrair();
  Extrair();

  PrintLista();
  
  LiberarLista();
  return 0;
}