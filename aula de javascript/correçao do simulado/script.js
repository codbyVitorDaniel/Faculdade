// ============================================
// ÁREA DE CÓDIGO PARA OS ALUNOS PREENCHEREM
// Todos os TODOs devem ser implementados neste arquivo
// ============================================

// ========== EXERCÍCIO 1: Adicionar Elemento via Input (1 ponto) ==========
// TODO 1: Implemente a funcionalidade completa para adicionar itens à lista
//         - Selecione o input (id: "textoItem"), o botão (id: "adicionarItem") e a lista (id: "listaItens")
//         - Adicione um event listener de 'click' ao botão
//         - Quando clicado, crie um novo elemento <li>, defina seu texto com o valor do input,
//           adicione à lista usando appendChild e limpe o campo de input

const inputItem = document.getElementById("textoItem");
const botaoAdicionar = document.getElementById("adicionarItem");
const listaItens = document.getElementById("listaItens");

botaoAdicionar.addEventListener("click", function () {
  const novoItem = document.createElement("li");
  novoItem.textContent = inputItem.value;
  listaItens.appendChild(novoItem);
  inputItem.value = "";
});

// ========== EXERCÍCIO 2: Manipular CSS pelo DOM (1 ponto) ==========
// TODO 2: Implemente a funcionalidade para alterar o estilo do quadrado
//         - Selecione o elemento quadrado (id: "quadrado") e o botão (id: "mudarEstilo")
//         - Adicione um event listener de 'click' ao botão
//         - Quando clicado, altere: backgroundColor para "lightblue", width para "200px",
//           height para "200px" e borderRadius para "10px"

const quadrado = document.getElementById("quadrado");
const botaoMudar = document.getElementById("mudarEstilo");

botaoMudar.addEventListener("click", function () {
  quadrado.style.backgroundColor = "lightblue";
  quadrado.style.width = "200px";
  quadrado.style.height = "200px";
  quadrado.style.borderRadius = "10px";
});

// ========== EXERCÍCIO 3: Event Listeners de Teclado (2 pontos) ==========
// TODO 3: Implemente as três funções e seus event listeners de teclado
//         - Crie a função "aoPressionar" que atualiza o innerHTML do elemento id "resultadoKeydown" com "Tecla pressionada (keydown)"
//         - Crie a função "aoPressionando" que atualiza o innerHTML do elemento id "resultadoKeypress" com "Tecla pressionando (keypress)"
//         - Crie a função "aoSoltar" que atualiza o innerHTML do elemento id "resultadoKeyup" com "Tecla solta (keyup)"
//         - Adicione event listeners 'keydown', 'keypress' e 'keyup' ao document, cada um chamando sua respectiva função

function aoPressionar(event) {
  const elemento = document.getElementById("resultadoKeydown");
  elemento.innerHTML = "Tecla pressionada (keydown)";
}

function aoPressionando(event) {
  const elemento = document.getElementById("resultadoKeypress");
  elemento.innerHTML = "Tecla pressionando (keypress)";
}

function aoSoltar(event) {
  const elemento = document.getElementById("resultadoKeyup");
  elemento.innerHTML = "Tecla solta (keyup)";
}

document.addEventListener("keydown", aoPressionar);
document.addEventListener("keypress", aoPressionando);
document.addEventListener("keyup", aoSoltar);

// ========== EXERCÍCIO 4: Detalhes da Tecla Pressionada (2 pontos) ==========
// TODO 4: Implemente a função que mostra os detalhes da tecla pressionada
//         - Crie uma função "mostrarDetalhesTecla" que recebe um parâmetro "event"
//         - Dentro da função, selecione o elemento com id "detalhesTecla"
//         - Atualize o innerHTML exibindo: "Código: " + event.code, "Tecla: " + event.key,
//           "Shift: " + (event.shiftKey ? "Sim" : "Não"), "Control: " + (event.ctrlKey ? "Sim" : "Não")
//         - Use quebras de linha (<br>) entre cada informação
//         - Adicione um event listener 'keyup' ao document que chama "mostrarDetalhesTecla"

function mostrarDetalhesTecla(event) {
  const detalhes = document.getElementById("detalhesTecla");
  detalhes.innerHTML =
    "Código: " + event.code +
    "<br>" +
    "Tecla: " + event.key +
    "<br>" +
    "Shift: " + (event.shiftKey ? "Sim" : "Não") +
    "<br>" +
    "Control: " + (event.ctrlKey ? "Sim" : "Não");
}

document.addEventListener("keyup", mostrarDetalhesTecla);

// ========== EXERCÍCIO 5: Classes - Construtor e Métodos (2 pontos) ==========
// TODO 5: Implemente a classe Pessoa e a função testarPessoa
//         - Crie uma classe "Pessoa" com construtor que recebe "nome" e "idade"
//         - No construtor, defina this.nome = nome e this.idade = idade
//         - Crie um método "apresentar" que retorna: "Olá, meu nome é " + this.nome + " e tenho " + this.idade + " anos."
//         - Na função testarPessoa(), crie uma instância da classe Pessoa com nome "João" e idade 25,
//           chame o método apresentar() e exiba o resultado no elemento com id "resultadoPessoa"

class Pessoa {
  constructor(nome, idade) {
    this.nome = nome;
    this.idade = idade;
  }

  apresentar() {
    return "Olá, meu nome é " + this.nome + " e tenho " + this.idade + " anos.";
  }
}

// ========== FUNÇÕES DE TESTE ==========
// As funções abaixo são chamadas pelos botões do HTML
// Você deve implementar o código dentro delas conforme os TODOs acima

function testarPessoa() {
  const pessoa = new Pessoa("João", 25);
  const resultado = pessoa.apresentar();
  const elemento = document.getElementById("resultadoPessoa");
  elemento.innerHTML = resultado;
}
