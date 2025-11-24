// ============================================
// ÁREA DE CÓDIGO PARA OS ALUNOS PREENCHEREM
// Todos os TODOs devem ser implementados neste arquivo
// ============================================

// ========== EXERCÍCIO 1: Adicionar Elemento via Input (1,5 pontos) ==========
// TODO 1: Implemente a funcionalidade completa para adicionar itens à lista
//         - Selecione o input (id: "textoItem"), o botão (id: "adicionarItem") e a lista (id: "listaItens")
//         - Adicione um event listener de 'click' ao botão
//         - Quando clicado, crie um novo elemento <li>, defina seu texto com o valor do input,
//           adicione à lista usando appendChild e limpe o campo de input
const Item = document.getElementById("textoItem");
const botao = document.getElementById("adicionarItem");
const listaItens = document.getElementById("listaItens");

botao.addEventListener("click", function () {
  const foi = document.createElement("li");
  foi.textContent = Item.value;
  listaItens.appendChild(foi);
  Item.value = "";
});
// ========== EXERCÍCIO 2: Manipular CSS pelo DOM (1,5 pontos) ==========
// TODO 2: Implemente a funcionalidade para alterar o estilo do quadrado
//         - Selecione o elemento quadrado (id: "quadrado") e o botão (id: "mudarEstilo")
//         - Adicione um event listener de 'click' ao botão
//         - Quando clicado pela primeira vez, altere: backgroundColor para "red", width para "200px",
//           height para "200px" e borderRadius para "10px"
//         - Quando clicado novamente, o quadrado deve voltar ao estado original:
//           backgroundColor para "#ff6b6b", width para "100px", height para "100px" e borderRadius para "0px"
//         - Dica: use uma variável para controlar o estado (alternar entre original e modificado)
const qua = document.getElementById("quadrado");
const buton = document.getElementById("mudarEstilo");

buton.addEventListener("click", function () {
  qua.style.backgroundColor = "#ff6b6b";
  qua.style.width = "200px";
  qua.style.height = "200px";
  qua.style.borderRadius = "10px";
});
// ========== EXERCÍCIO 3: Event Listeners de Teclado (2 pontos) ==========
// TODO 3: Implemente as funções e event listeners de teclado unificados
//         - Crie funções para keydown, keypress e keyup que atualizem o elemento id "resultadoTeclado"
//         - Cada função deve exibir: a tecla pressionada (event.key) e qual evento está sendo executado
//         - Exemplo de formato: "Keydown: Tecla 'a' pressionada" ou "Keypress: Tecla 'a' pressionada" ou "Keyup: Tecla 'a' pressionada"
//         - Adicione event listeners 'keydown', 'keypress' e 'keyup' ao document, cada um chamando sua respectiva função
//         - Todas as informações devem ser exibidas na mesma área de resultado (id: "resultadoTeclado")
function Pressionar(event) {
  const elemento = document.getElementById("resultadoTeclado");
  elemento.innerHTML = "keydown";
}

function Pressionando(event) {
  const elemento = document.getElementById("resultadoTeclado");
  elemento.innerHTML = "keypress";
}

function Soltar(event) {
  const elemento = document.getElementById("resultadoTeclado");
  elemento.innerHTML = "keyup";
}

document.addEventListener("keydown", Pressionar);
document.addEventListener("keypress", Pressionando);
document.addEventListener("keyup", Soltar);

function Tecla(event) {
  const detalhes = document.getElementById("resultadoTeclado");
  detalhes.innerHTML =
    "Código: " + event.code +
    "<br>" +
    "Tecla: " + event.key +
    "<br>" +
    "Shift: " + (event.shiftKey ? "Sim" : "Não") +
    "<br>" +
    "Control: " + (event.ctrlKey ? "Sim" : "Não");
}

document.addEventListener("keyup", Tecla);

// ========== EXERCÍCIO 4: Classes - Construtor e Métodos com Formulário (3 pontos) ==========
// TODO 4: Implemente a classe Pessoa e a função testarPessoa
//         - Crie uma classe "Pessoa" com construtor que recebe "nome", "idade" e "bairro"
//         - No construtor, defina this.nome = nome, this.idade = idade e this.bairro = bairro
//         - Crie um método "apresentar" que retorna: "Prazer, meu nome é " + this.nome + ", tenho " + this.idade + " anos e moro em " + this.bairro + " - RJ."
//         - Na função testarPessoa(), obtenha os valores dos inputs (id: "nomePessoa", "idadePessoa", "bairroPessoa")
//         - Crie uma instância da classe Pessoa com os valores obtidos do formulário
//         - Chame o método apresentar() e exiba o resultado no elemento com id "resultadoPessoa"

class Pessoa {
  constructor(nome, idade, bairro) {
    this.nome = nome;
    this.idade = idade;
    this.bairro = bairro;
  }

  apresentar() {
    let nome = this.nome;
    let idade = this.idade;
    let bairro = this.bairro;
    const elemento = document.getElementById("resultadoPessoa");
    elemento.innerHTML = nome;
    elemento.innerHTML = idade;
    elemento.innerHTML = bairro;
    return "Prazer, meu nome é  " + this.nome + " tenho " + this.idade + " anos e moro em " + this.bairro + "- RJ.";
  }
}
function testarPessoa() {

  const pessoa = new Pessoa(this.nome, this.idade, this.bairro);
  const resultado = pessoa.apresentar();
  const elemento = document.getElementById("resultadoPessoa");
  elemento.innerHTML = resultado;
}
// ========== FUNÇÕES DE TESTE ==========
// As funções abaixo são chamadas pelos botões do HTML
// Você deve implementar o código dentro delas conforme os TODOs acima



// Pontos Extras:
// 0,5 pontos extras:
// -> Adicione um botão para remover o item, ao lado do item adicionado no exercício 1.


