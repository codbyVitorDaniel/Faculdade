let nota = 7;

if (nota >= 6){
    console.log("Aprovado")
} else{
    console.log("Reprovado")
}

console.log(nota == "7")
console.log(nota === "7")
console.log(nota != "5")
console.log(nota >= "7")


// let situaçao = nota >= 5.5 ? "Aprovado" : "Reprovado"
// console.log(situaçao)

let frutas = "Manga"
switch (nota) {
    case nota >= 6:
        console.log("Aprovado")
        break;
    case nota <= 6 && nota >= 4:
        console.log("Esta em recuperaçao")
        break;
    case nota < 4:
        console.log("Reprovado")
        break
}