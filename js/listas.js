// tendo uma lista ordenada, adicione um número da forma que a lista se mantenha ordenada

// ordenando lista
const lista = [15, 23, 2, 18, 10, 21, 17, 3, 19, 16];

function OrdenarLista(lista) {
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
}


// adicionar um número e manter ordenado
const lista2 = [1,6,7,11,13,15,16,18,27,35,46];
let numPendente = 0;
let maiorNumProx = lista2[lista2.length -1];
let indice = lista2.indexOf(maiorNumProx);

for (const numero of lista2) {
    if ((numero < maiorNumProx && numero > numPendente)) {
        maiorNumProx = numero;
        indice = lista2.indexOf(maiorNumProx);
    }
}
// lista2.splice(indice,0,numPendente);
// console.log(maiorNumProx);
console.log(lista2);


///////////////////////////////////////////
// lista2 = [1,3,5,7,8,10,12,16,25,36,]
// proxNum = lista2[-1]

// for indice,item in lista2[::-1]:
//     if lista[indice] == None:
//         lista[indice] = numero_pendente
//     elif item > numero_pendente:
//         lista2[indice+1] = item
//     elif item < numero_pendente:
//         lista2[indice] = numero_pendente

let lista3 = [1,3,5,7,8,10,12,16,25,36,];
let proxNum = lista2[lista3.length - 1]

for (let d = lista3.length; d < lista3.length; d--) {
    if lista3[d]
}