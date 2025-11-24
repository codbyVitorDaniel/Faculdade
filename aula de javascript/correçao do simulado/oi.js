// ============================================
// GABARITO COMPLETO - script.js
// Respostas esperadas para cada TODO
// ============================================

// ========== EXERCÃCIO 1: Adicionar Elemento via Input (1 ponto) ==========
// TODO 1: Implemente a funcionalidade completa para adicionar itens Ã  lista
const inputItem = document.getElementById("textoItem");
const botaoAdicionar = document.getElementById("adicionarItem");
const listaItens = document.getElementById("listaItens");

botaoAdicionar.addEventListener("click", () => {
  const novoItem = document.createElement("li");
  novoItem.textContent = inputItem.value;
  listaItens.appendChild(novoItem);
  inputItem.value = "";
});

// ========== EXERCÃCIO 2: Manipular CSS pelo DOM (1 ponto) ==========
// TODO 2: Implemente a funcionalidade para alterar o estilo do quadrado
const quadrado = document.getElementById("quadrado");
const botaoMudar = document.getElementById("mudarEstilo");

botaoMudar.addEventListener("click", () => {
  quadrado.style.backgroundColor = "lightblue";
  quadrado.style.width = "200px";
  quadrado.style.height = "200px";
  quadrado.style.borderRadius = "10px";
});

// ========== EXERCÃCIO 3: Event Listeners de Teclado (2 pontos) ==========
// TODO 3: Implemente as trÃªs funÃ§Ãµes e seus event listeners de teclado
function aoPressionar(event) {
  document.getElementById("resultadoKeydown").innerHTML =
    "Tecla pressionada (keydown)";
}

function aoPressionando(event) {
  document.getElementById("resultadoKeypress").innerHTML =
    "Tecla pressionando (keypress)";
}

function aoSoltar(event) {
  document.getElementById("resultadoKeyup").innerHTML = "Tecla solta (keyup)";
}

document.addEventListener("keydown", aoPressionar);
document.addEventListener("keypress", aoPressionando);
document.addEventListener("keyup", aoSoltar);

// ========== EXERCÃCIO 4: Detalhes da Tecla Pressionada (2 pontos) ==========
// TODO 4: Implemente a funÃ§Ã£o que mostra os detalhes da tecla pressionada
function mostrarDetalhesTecla(event) {
  const elemento = document.getElementById("detalhesTecla");
  elemento.innerHTML =
    "CÃ³digo: " + event.code +
    "<br>" +
    "Tecla: " + event.key +
    "<br>" +
    "Shift: " + (event.shiftKey ? "Sim" : "NÃ£o") +
    "<br>" +
    "Control: " + (event.ctrlKey ? "Sim" : "NÃ£o");
}

document.addEventListener("keyup", mostrarDetalhesTecla);

// ========== EXERCÃCIO 5: Classes - Construtor e MÃ©todos (2 pontos) ==========
// TODO 5: Implemente a classe Pessoa e a funÃ§Ã£o testarPessoa
class Pessoa {
  constructor(nome, idade) {
    this.nome = nome;
    this.idade = idade;
  }

  apresentar() {
    return "OlÃ¡, meu nome Ã© " + this.nome + " e tenho " + this.idade + " anos.";
  }
}

function testarPessoa() {
  const pessoa = new Pessoa("JoÃ£o", 25);
  const resultado = pessoa.apresentar();
  document.getElementById("resultadoPessoa").innerHTML = resultado;
}