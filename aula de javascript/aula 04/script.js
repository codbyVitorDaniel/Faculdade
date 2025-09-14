// let personagem = {
//     nome : "Vitor",
//     idade : "09",
//     pais: "Brasil"
// }
// console.log(`${personagem.nome} tem ${personagem.idade} anos de idade`)

// let personagem = {
//     nome:"Elfo arqueiro",
//     idade:"198",
//     pais:"Elven",
//     olhos:["azul","Vermelho","Negros"],
//     caracteristicas:{
//         estamina: 300,
//         forca: 90,
//         pdef: 200,
//         mdef: 350,
//         patack: 1200,
//         mana: 450,
//     }
// }

// personagem.nome = "Elfo Tanker"
// personagem.caracteristicas.pdef = 20000
// personagem.caracteristicas.patack = 300
// personagem.olhos.push("verdes")//Adiciona um novo item na lista composta

// console.log(`
//     O personagem: ${personagem.nome}
//     e ele tem olhos ${personagem.olhos[1]}
//     Possui:
//         ----------------------
//         |Mana:${personagem.caracteristicas.mana}
//         |Força:${personagem.caracteristicas.forca}
//         |Estamina:${personagem.caracteristicas.estamina}
//         |Desfesa:${personagem.caracteristicas.pdef}
//         |Defesa Magica:${personagem.caracteristicas.mdef}
//         |Ataque:${personagem.caracteristicas.patack}
//         ----------------------
//     `)







// let pessoa = {
//     nome:"Prof.tiago",
//     idade: 45,
//     carros: [
//         {modelo: "Fiat", cor:"Cinza"},
//         {modelo: "BMW", cor: "Branco"},
//         {modelo: "BYD", cor: "Preto"}
//     ]
// }

// console.log(pessoa.carros[0].cor)

// let pessoa = {
//     nome:"Tiago",
//     sobrenome:"Castro",
//     idade:35,


//     nomeCompleto :function () {
//         return `${this.nome} ${this.sobrenome}`        
//     }
// }

// console.log(pessoa.nomeCompleto())


// //outro
// //"azul", "Amarelo", "Vermelho", "Verde"
// cores = [
//     {nome:"azul", qt:10},
//     {nome:"amarelo", qt:10},
//     {nome:"vermelho", qt:10},
//     {nome:"verde", qt:9}
    
//     ]
// // for (let n = 0; n <= 10;n++){
// //     console.log(`Contando: ${cores[n]}`)
// // }
// // for (let cor of cores){
// //     console.log(`Contando: ${cores[cor]}`)
// // }


// // //outro
// // for (let cor of cores){
// //     console.log(`Dar cor: ${cor.nome.toUpperCase()} eu tenho: ${cor.qt} unid.`)

// // }


// contador = 0 
// while(contador < cores.lenght){
//     console.log(`${cores[contador].nome}`)
//     contador ++
// }




// //faça um loop que monstre todas as frutas da lista abaixo.
// // e tambem sua posiçao no console
// let frutas = ["Banana", "Maça", "Uva", "Abacate"]

// // for (let fruta in frutas){
// //     console.log(`Fruta na posiçao ${fruta}: ${frutas[fruta]}`)
// // }

// console.log(frutas.length)
// frutas.push("Abacaxi")
// console.log(frutas)
// frutas.pop();
// console.log(frutas);
// frutas.shift();
// console.log(frutas);
// console.log(frutas);
// console.log(frutas.join(" -> "))

// let frutas = ["banana", "Maça", "Uva", "Abacate", "Abacaxi"];
// for (let fruta in frutas){
//     if (frutas[fruta] == "Abacate"){
//         fruta[fruta] = "morango"
//     }
// // }
// let frutas = ["banana", "Maça", "Uva", "Abacate", "Abacaxi"];
// frutas.sort()
// console.log()

let cars = [
    {brand:"Fiat", years:2003},
    {brand:"fox", years:2003},
    {brand:"Fiat", years:2003},
    
]

cars.sort((a,b) => {
    if (a.years > b.years){
        return 1;
        }else if (a.years < b.years){
            return -1;
        }else{
            return0;
        }

})
cars.sort((a , b) => a.years - b.years)

console.log(cars)