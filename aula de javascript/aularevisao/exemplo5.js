let titulo = document.getElementById("titulo")
let itens = document.getElementsByTagName("li")
let lista = document.querySelector(".lista")
let todos = document.querySelectorAll(".lista li")

console.log(titulo.innerText);
console.log(itens.length);
console.log(lista.innerHTML);
console.log(todos)



// manipulaçoes
titulo.innerText = "Adicionei um Novo Titulo"
lista.append(" + um texto")

let botao = document.getElementById("btn")
let resultado = document.getElementById("resultado")

botao.addEventListener("click", () =>
{
    resultado.innerHTML = "<b> Voce clicou no boato<b>"
})