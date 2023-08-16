// tendo uma lista ordenada, adicione um número da forma que a lista se mantenha ordenada

// ordenando lista
const lista = [15, 23, 2, 18, 10, 21, 17, 3, 19, 16];

// criando lista que vai ser ordenada
const listaOrdenada = [];
const tamanhoLista = lista.length;
let indice;
let menorNum;

for (let j = 0; j < tamanhoLista; j++) {
    menorNum = lista[0]
    indice = 0
    for(let i = 0; i < lista.length; i ++){
        if (menorNum > lista[i]) {
            menorNum = lista[i];  
            indice = lista.indexOf(menorNum);
        }
    }
    lista.splice(indice,1);
    listaOrdenada.push(menorNum);
}
console.log("lista " + lista);
console.log("lista ordenada " + listaOrdenada);