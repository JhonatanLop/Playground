#include <stdio.h>
#include <stdlib.h>

struct branch {
    int value;
    struct branch *right;
    struct branch *left;
};

branch create_branch(int value){
    branch* new_branch = (branch*)malloc(sizeof(branch));
    new_branch->value = value;
    new_branch->right = NULL;
    new_branch->left = NULL;
    return new_branch;
};

void add_branch(branch* raiz, int value) {
    if (raiz == NULL) {
        raiz = create_branch(value);
    }

    if (value < raiz->value){
        raiz->left = add_branch(raiz->left, value)
    } else {
        raiz->right = add_branch(raiz->right, value)
    }
    
}

int main() {
branch raiz = NULL;
raiz = add_branch(raiz, 4);
}