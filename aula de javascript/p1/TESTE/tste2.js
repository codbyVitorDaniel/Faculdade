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
    let m = document.getElementById("input-titulo")
    const h1 = document.getElementById("titulo-principal")
    
    h1.textContent = m.value
    m.value = "";

    // TODO: 
    // 1. Pegar o valor do input com id "input-titulo"
    // 2. Pegar o elemento H1 com id "titulo-principal"  
    // 3. Alterar o innerText do H1 com o valor do input
    // 4. Limpar o input após a alteração
    
    // DICA: Use getElementById() e innerText
    // DICA: Use value para pegar o conteúdo do input
    
    // SEU CÓDIGO AQUI:
    
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
    let input = document.getElementById("input-item")
    let valor_input = input.value
    if (valor_input == ""){
        alert("Nao pode estar sem nada")
    }

    const lista = document.getElementById("lista-itens")
    const li = document.createElement("li")
    li.innerHTML=input.value
    //const valor = li.textContent
    lista.appendChild(input)
    valor_input.value = ""
    
}

// ===========================================
// EXERCÍCIO 3: CALCULADORA DE SOMAS
// ===========================================
// Objetivo: Somar dois números e exibir o resultado na lista de cálculos

function calcularSoma() {
    // TODO:
    // 1. Pegar os valores dos inputs com id "numero1" e "numero2"
    
    let numero1 = document.getElementById("numero1")
    let numero2 = document.getElementById("numero2")
    // 2. Converter os valores para números usando Number() ou parseInt()
    
    const valor1 = parseFloat(numero1.value)
    const valor2 = parseFloat(numero2.value)
    
    
    
    // 3. Verificar se ambos os valores são números válidos
   // if (isNumber(valor1) && isNumber(valor2)){
   //     alert("Fucionou")
   // }else{
   //     alert("So aceita numeros")
    //}
    // 4. Calcular a soma
    const soma = valor1 + valor2
    
    // 5. Criar um novo <li> com o texto da operação (ex: "5 + 3 = 8")
    const novoli = document.createElement("li");
    novoli.textContent = `${valor1} + ${valor2} = ${soma}`
    
    // 6. Adicionar o <li> à lista com id "lista-calculos"
    const novoitem = document.getElementById("lista-calculos")
    novoitem.appendChild(novoli)
    alert(novoli.textContent)
    // 7. Limpar os inputs após o cálculo
    numero1.value = ""
    numero2.value = ""
    
    // DICA: Use Number() para converter string para número
    // DICA: SE QUISER Use isNaN() para verificar se é um número válido (NÃO OBRIGATÓRIO) <<<<
    // DICA: Template string: `${num1} + ${num2} = ${resultado}`
    
    // SEU CÓDIGO AQUI:
    

   
    

}

// ===========================================
// EXERCÍCIO 4: CONTADOR DE ITENS
// ===========================================
// Objetivo: Contar quantos itens existem nas listas e exibir no corpo da página

function contarItens() {
    // TODO:
    // 1. Pegar todas as listas <ul> da página
    const pegar = document.querySelectorAll("ul")
    // 2. Para cada lista, contar quantos <li> ela possui
    let cont = []
    soma = 0
    cont.push( pegar.length);
    // 3. Somar o total de itens de todas as listas
    for (let i = 0; i < pegar.length; i++){
        soma = pegar + soma
    }
    // 4. Exibir o resultado na div com id "resultado-contador"
    const div = document.getElementById("resultado-contador")
    div.innerHTML(`O total de item e ${soma}`)
    // 5. O resultado deve mostrar: "Total de itens: X"
    // 6. Adicionar também: "Lista 1: X itens", "Lista 2: Y itens", etc.
    
    // DICA: Use querySelectorAll("ul") para pegar todas as listas
    // DICA: Use querySelectorAll("li") dentro de cada lista para contar
    // DICA: Use forEach() para iterar sobre as listas
    // DICA: Use innerHTML para adicionar HTML formatado
    
    // SEU CÓDIGO AQUI:
    
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