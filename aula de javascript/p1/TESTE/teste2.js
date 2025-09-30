// ===========================================
// SIMULADO JAVASCRIPT - FRONT-END
// ===========================================
// Este arquivo contém o esqueleto para os exercícios
// Complete as funções conforme as instruções

// ===========================================
// EXERCÍCIO 1: MODIFICAR TÍTULO DA PÁGINA
// ===========================================

function alterarTitulo() {
    let input = document.getElementById("input-titulo");
    let novoTitulo = input.value;

    let h1 = document.getElementById("titulo-principal");
    h1.innerText = novoTitulo;

    input.value = "";
}

// ===========================================
// EXERCÍCIO 2: ADICIONAR ITENS À LISTA
// ===========================================

function adicionarItem() {
    let input = document.getElementById("input-item");
    let valor = input.value.trim();

    if (valor === "") {
        return;
    }

    let novoItem = document.createElement("li");
    novoItem.textContent = valor;

    let lista = document.getElementById("lista-itens");
    lista.appendChild(novoItem);

    input.value = "";
}

// ===========================================
// EXERCÍCIO 3: CALCULADORA DE SOMAS
// ===========================================

function calcularSoma() {
    let n1 = Number(document.getElementById("numero1").value);
    let n2 = Number(document.getElementById("numero2").value);

    if (isNaN(n1) || isNaN(n2)) {
        alert("Digite apenas números!");
        return;
    }

    let li = document.createElement("li");
    li.textContent = `${n1} + ${n2} = ${n1 + n2}`;

    document.getElementById("lista-calculos").appendChild(li);

    document.getElementById("numero1").value = "";
    document.getElementById("numero2").value = "";
}

// ===========================================
// EXERCÍCIO 4: CONTADOR DE ITENS
// ===========================================

function contarItens() {
    let listas = document.querySelectorAll("ul");
    let resultado = document.getElementById("resultado-contador");

    let total = 0;
    let texto = "";

    listas.forEach(function(lista, index) {
        let itens = lista.querySelectorAll("li").length;
        total += itens;
        texto += "Lista " + (index + 1) + ": " + itens + " itens<br>";
    });

    texto = "Total de itens: " + total + "<br>" + texto;

    resultado.innerHTML = texto;
  document.getElementById("btn-contar").addEventListener("click", contarItens);
}

// ===========================================
// EVENT LISTENERS - NÃO MODIFICAR
// ===========================================

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('btn-alterar-titulo').addEventListener('click', alterarTitulo);
    document.getElementById('btn-adicionar-item').addEventListener('click', adicionarItem);
    document.getElementById('btn-calcular').addEventListener('click', calcularSoma);
    document.getElementById('btn-contar').addEventListener('click', contarItens);
});

// ===========================================
// EXERCÍCIOS EXTRAS (OPCIONAIS)
// ===========================================

// Validar se input não está vazio
function validarInput(input) {
    if (input.value.trim() === "") {
        return false;
    }
    return true;
}

// Limpar todos os inputs da página
function limparTodosInputs() {
    let inputs = document.querySelectorAll("input");
    inputs.forEach(function(input) {
        input.value = "";
    });
}

// Remover o último item da lista de itens
function removerUltimoItem() {
    let lista = document.getElementById("lista-itens");
    if (lista.lastChild) {
        lista.removeChild(lista.lastChild);
    }
}
