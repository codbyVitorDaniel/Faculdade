let fruta = ["Banana", "Maça", "Pera", "Uva"];

fruta.pop(); // Remove o último item da lista
fruta.push("Abacate"); // Adiciona "Abacate"
fruta.shift(); // Remove o primeiro item da lista
console.log(fruta.join(" - ")); // Exibe a lista

let numeros = [1, 1000, 250, 3, 9, 28, 55];
console.log(numeros.sort((a, b) => a - b)); // Ordena numericamente de forma crescente
console.log(numeros.reverse()); // Ordena de forma decrescente

//iteraçao
for (let i = 0; i < frutas.length; i++){
    console.log(frutas[i])
}

let i = 0;
while (i < frutas.length) {
    console.log("While: ", fruta[i])
    i ++ ;

}
for (let a of frutas){
    console.log("for ... of:", fruta);
}