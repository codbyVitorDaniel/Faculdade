
// ===========================================
// SIMULADO JAVASCRIPT - FRONT-END
// ===========================================
// Este arquivo contém o esqueleto para os exercícios
// Complete as funções conforme as instruções

// ===========================================
// EXERCÍCIO 1: MODIFICAR TÍTULO DA PÁGINA
// ===========================================
// Objetivo: Pegar o valor do input e alterar o título da página (H1)

function alterarTitulo() {
    // 1. Pegar o valor do input com id "input-titulo"
    var input = document.getElementById("input-titulo");
    var novoTitulo = input.value;

    // 2. Pegar o elemento H1 com id "titulo-principal"
    var h1 = document.getElementById("titulo-principal");

    // 3. Alterar o innerText do H1 com o valor do input
    h1.innerText = novoTitulo;

    // 4. Limpar o input após a alteração
    input.value = "";
}

// ===========================================
// EXERCÍCIO 2: ADICIONAR ITENS À LISTA
// ===========================================
// Objetivo: Pegar o valor do input e adicionar como novo item na lista

function adicionarItem() {
    // 1. Pegar o valor do input com id "input-item"
    let input = document.getElementById("input-item");
    let valor = input.value.trim();

    // 2. Verificar se o input não está vazio
    if (valor === "") {
        return;
    }

    // 3. Criar um novo elemento <li> usando createElement
    let novoItem = document.createElement("li");

    // 4. Definir o textContent do <li> com o valor do input
    novoItem.textContent = valor;

    // 5. Adicionar o <li> à lista usando appendChild
    let lista = document.getElementById("lista-itens");
    lista.appendChild(novoItem);

    // 6. Limpar o input após adicionar
    input.value = "";
}

// ===========================================
// EXERCÍCIO 3: CALCULADORA DE SOMAS
// ===========================================
// Objetivo: Somar dois números e exibir o resultado na lista de cálculos

function calcularSoma() {
    // 1. Pegar os valores dos inputs com id "numero1" e "numero2"
    let input1 = document.getElementById("numero1");
    let input2 = document.getElementById("numero2");

    // 2. Converter os valores para números usando Number()
    let num1 = Number(input1.value);
    let num2 = Number(input2.value);

    // 3. Verificar se ambos os valores são números válidos
    if (isNaN(num1) || isNaN(num2)) {
        return;
    }

    // 4. Calcular a soma
    let resultado = num1 + num2;
    let resultado2 = num1 -  num2;
    let resultado3 = num1 *  num2;
    let resultado4 = num1 /  num2;


    // 5. Criar um novo <li> com o texto da operação
    let novoCalculo = document.createElement("li");
    novoCalculo.textContent = num1 + " + " + num2 + " = " + resultado;
    // ou para subtração:
    let novoCalculo2 = document.createElement("li");
    novoCalculo2.textContent = num1 + " - " + num2 + " = " + resultado2;
    // ou para multiplicação:
    let novoCalculo3 = document.createElement("li");
    novoCalculo3.textContent = num1 + " * " + num2 + " = " + resultado3;
    // ou para divisão:
    let novoCalculo4 = document.createElement("li");
    novoCalculo4.textContent = num1 + " / " + num2 + " = " + resultado4;

    // 6. Adicionar o <li> à lista com id "lista-calculos"
    let lista = document.getElementById("lista-calculos");
    lista.appendChild(novoCalculo);
    lista.appendChild(novoCalculo2);
    lista.appendChild(novoCalculo3);
    lista.appendChild(novoCalculo4);

    // 7. Limpar os inputs após o cálculo
    input1.value = "";
    input2.value = "";


// ou esse código abaixo:
//    let n1 = Number(document.getElementById("numero1").value);
//     let n2 = Number(document.getElementById("numero2").value);
//     let li = document.createElement("li");
//     li.textContent = `${n1} + ${n2} = ${n1 + n2}`;
//     li.textContent = `${n1} + ${n2} = ${n1 - n2}`;
//     document.getElementById("lista-calculos").appendChild(li);
//     document.getElementById("numero1").value = "";
//     document.getElementById("numero2").value = "";
}

// ===========================================
// EXERCÍCIO 4: CONTADOR DE ITENS
// ===========================================
// Objetivo: Contar quantos itens existem nas listas e exibir no corpo da página

function contarItens() {
    // TODO:
    // 1. Pegar todas as listas <ul> da página
    // 2. Para cada lista, contar quantos <li> ela possui
    // 3. Somar o total de itens de todas as listas
    // 4. Exibir o resultado na div com id "resultado-contador"
    // 5. O resultado deve mostrar: "Total de itens: X"
    // 6. Adicionar também: "Lista 1: X itens", "Lista 2: Y itens", etc.
    
    // DICA: Use querySelectorAll("ul") para pegar todas as listas
    // DICA: Use querySelectorAll("li") dentro de cada lista para contar
    // DICA: Use forEach() para iterar sobre as listas
    // DICA: Use innerHTML para adicionar HTML formatado
    
    // SEU CÓDIGO AQUI:

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
    
}

// ===========================================
// EVENT LISTENERS - NÃO MODIFICAR <<<<<<<<<<
// ===========================================
// Estes event listeners conectam os botões às funções
// NÃO ALTERE ESTA SEÇÃO <<<<<<<<<<


document.addEventListener('DOMContentLoaded', function() {
    // Exercício 1
    document.getElementById('btn-alterar-titulo').addEventListener('click', alterarTitulo);
    
    // Exercício 2  
    document.getElementById('btn-adicionar-item').addEventListener('click', adicionarItem);
    
    // Exercício 3
    document.getElementById('btn-calcular').addEventListener('click', calcularSoma);
    
    // Exercício 4
    document.getElementById('btn-contar').addEventListener('click', contarItens);
});

// ===========================================
// EXERCÍCIOS EXTRAS (OPCIONAIS) (NAO OBRIGATORIO) <<<<<<<<<<
// ===========================================

// Função para validar se um input não está vazio
function validarInput(input) {
    // TODO: Implementar validação
    // Retornar true se o input não estiver vazio
    // Retornar false se estiver vazio

    // SEU CÓDIGO AQUI:
    let valor = input.value;
    if (valor.trim() !== "") {
        return true;
    } else {
        return false;
    }
}


// Função para limpar todos os inputs da página
function limparTodosInputs() {
    // Pega todos os elementos input da página
    let inputs = document.getElementsByTagName("input");
    // Para cada input, limpa o valor
    for (let i = 0; i < inputs.length; i++) {
        inputs[i].value = "";
    }
}

// Função para remover o último item da lista
function removerUltimoItem() {
    // TODO: Implementar remoção
    // Remover o último <li> da lista de itens
    
    // SEU CÓDIGO AQUI:
    
}
