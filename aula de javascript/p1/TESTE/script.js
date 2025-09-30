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
    // TODO: 
    // 1. Pegar o valor do input com id "input-titulo"
    // 2. Pegar o elemento H1 com id "titulo-principal"  
    // 3. Alterar o innerText do H1 com o valor do input
    // 4. Limpar o input após a alteração
    
    // DICA: Use getElementById() e innerText
    // DICA: Use value para pegar o conteúdo do input
    
    // SEU CÓDIGO AQUI:
    let input = document.getElementById("input-titulo");
    let novoTitulo = input.value;
   
    let h1 = document.getElementById("titulo-principal");
    h1.innerText = novoTitulo;
    input.value = "";
    
}

// ===========================================
// EXERCÍCIO 2: ADICIONAR ITENS À LISTA
// ===========================================
// Objetivo: Pegar o valor do input e adicionar como novo item na lista

function adicionarItem() {
    // TODO:
    // 1. Pegar o valor do input com id "input-item"
    // 2. Verificar se o input não está vazio
    // 3. Criar um novo elemento <li> usando createElement
    // 4. Definir o textContent do <li> com o valor do input
    // 5. Adicionar o <li> à lista usando appendChild
    // 6. Limpar o input após adicionar
    
    // DICA: Use createElement("li"), textContent, appendChild
    // DICA: Use trim() para remover espaços em branco
    
    // SEU CÓDIGO AQUI:
    
   
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
// Objetivo: Somar dois números e exibir o resultado na lista de cálculos

function calcularSoma() {
    // TODO:
    // 1. Pegar os valores dos inputs com id "numero1" e "numero2"
    // 2. Converter os valores para números usando Number() ou parseInt()
    // 3. Verificar se ambos os valores são números válidos
    // 4. Calcular a soma
    // 5. Criar um novo <li> com o texto da operação (ex: "5 + 3 = 8")
    // 6. Adicionar o <li> à lista com id "lista-calculos"
    // 7. Limpar os inputs após o cálculo
    
    // DICA: Use Number() para converter string para número
    // DICA: SE QUISER Use isNaN() para verificar se é um número válido (NÃO OBRIGATÓRIO) <<<<
    // DICA: Template string: `${num1} + ${num2} = ${resultado}`
    
    // SEU CÓDIGO AQUI:

    let n1 = Number(document.getElementById("numero1").value);
    let n2 = Number(document.getElementById("numero2").value);
    let li = document.createElement("li");
    li.textContent = `${n1} + ${n2} = ${n1 + n2}`;
    document.getElementById("lista-calculos").appendChild(li);
    document.getElementById("numero1").value = "";
    document.getElementById("numero2").value = "";

    
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
    
}

// Função para limpar todos os inputs da página
function limparTodosInputs() {
    // TODO: Implementar limpeza
    // Pegar todos os inputs e limpar seus valores
    
    // SEU CÓDIGO AQUI:
    
}

// Função para remover o último item da lista
function removerUltimoItem() {
    // TODO: Implementar remoção
    // Remover o último <li> da lista de itens
    
    // SEU CÓDIGO AQUI:
    
}
