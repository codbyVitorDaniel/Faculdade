
// ===========================================
// SIMULADO JAVASCRIPT - CALCULADORA DE NOTAS
// ===========================================
// Este arquivo contém o esqueleto para as questões
// Complete as funções conforme as instruções

//const { createElement } = require("react")

// ===========================================
// EXERCÍCIO 1: ADICIONAR NOTA
// ===========================================
// Objetivo: Pegar o valor do input e adicionar como nova nota na lista
// TODO:
function adicionarNota() {
  // 1. Pegar o valor do input
  // 2. Verificar se o input não está vazio
  // 3. Converter para número e validar
  // 4. Criar novo <li>
  // 5. Colocar o valor da nota dentro do <li>
  // 6. Adicionar <li> na lista
  // 7. Limpar o input
  let input = document.getElementById("input-nota");
  let valor = input.value.trim();
  if (valor === "") {
    alert("A nota nao pode estar vazio");
    return;
  }
  let nota = Number(valor);
  if (isNaN(nota) || nota < 0 || nota > 10) {
    alert("Digite um numero entre 0 e 10");
    return;
  }
  let li = document.createElement("li");
  li.textContent = nota;
  let list = document.getElementById("listas das notas");
  list.appendChild(li);
  input.value = "";
}
// DICA: Use getElementById(), createElement("li"), textContent, appendChild
// DICA: Use Number() para converter string para número
// DICA: Use trim() para remover espaços em branco
// SEU CÓDIGO AQUI EMBAIXO:
// ===========================================
// EXERCÍCIO 2: CALCULAR MÉDIA
// ===========================================
function calcularMedia() {
  // 1. Pegar todas as notas (li dentro da lista)
  // 2. Somar as notas
  // 3. Calcular média
  // 4. Mostrar resultado
  let not = document.querySelectorAll("#lista-notas li");
  if (not.length === 0) {
    alert("Adicione notas primeiro!");
    return;
  }
  let som = 0;
  for (let i = 0; i < not.length; i++) {
    som += parseFloat(not[i].textContent);
  }
  let med = som / not.length;
  let result = document.getElementById("Resultado da media");
  result.textContent = `Média: ${med.toFixed(1)}`;
}
// DICA: Use querySelectorAll("li") para pegar todas as notas
// DICA: Use for (let i = 0; i < notas.length; i++) para iterar sobre as notas
// DICA: Use parseFloat() para converter texto para número
// DICA: Se quiser, Use toFixed(1) para arredondar para 1(uma) casa decimal 
// use getElementById() para adicionar o conteudo do id "resultado-media"
// DICA: use template strings para formatação dos resultados
// SEU CÓDIGO AQUI EMBAIXO:

// ===========================================
// EXERCÍCIO 3: VERIFICAR APROVAÇÃO
// ===========================================
// Objetivo: Verificar se o aluno foi aprovado (média >= 6.0)
function verificarAprovacao() {
  let notas = document.querySelectorAll("#lista-notas li");
  if (notas.length === 0) {
    alert("Adicione notas primeiro!");
    return;
  }
  let soma = 0;
  for (let i = 0; i < notas.length; i++) {
    soma += parseFloat(notas[i].textContent);
  }
  let media = soma / notas.length;
  let result = document.getElementById("resultado-aprovacao");
  if (media >= 6.0) {
    result.innerHTML = `Aprovado! (Média: ${media.toFixed(1)})`;
    result.className = "aprovado";
  } else {
    result.innerHTML = `Reprovado! (Média: ${media.toFixed(1)})`;
    result.className = "reprovado";
  }
}
// TODO:
// 1. Calcular a média das notas (reutilizar lógica do exercício 2)
// 2. Verificar se a média é >= 6.0
// 3. Exibir "Aprovado" ou "Reprovado" na div com id "resultado-aprovacao"
// 4. Adicionar classe CSS apropriada (aprovado/reprovado) << CODIGO ABAIXO:
// utilize resultado.className = "aprovado"; ou resultado.className = "reprovado";
// DICA: Use innerHTML para adicionar HTML
// DICA: Use o exemplo citado para adicionar classes CSS 
// dentro de uma estrutura if / else = (resultado.className = "aprovado" ou resultado.className = "reprovado")
// DICA: Use template strings para formatação
// use getElementById() para adicionar o conteudo do id "resultado-aprovacao"
// SEU CÓDIGO AQUI EMBAIXO:

// ===========================================
// EXERCÍCIO 4: ESTATÍSTICAS DAS NOTAS
// ===========================================
// Objetivo: Gerar estatísticas das notas e exibir na div de resultados

function gerarEstatisticas() {
  let notas = document.querySelectorAll("#lista-notas li");
  if (notas.length === 0) {
    alert("Adicione notas primeiro!");
    return;
  }
  let val = [];
  for (let i = 0; i < notas.length; i++) {
    val.push(parseFloat(notas[i].textContent));
  }
  let quant = val.length;
  let soma = 0;
  for (let i = 0; i < val.length; i++) {
    soma += val[i];
  }
  let media = soma / quant;
  let maior = Math.max(...val);
  let menor = Math.min(...val);
  let result = document.getElementById("resultado-estatisticas");
  result.innerHTML = `
    Quantidade: ${quant}<br>
    Média: ${media.toFixed(1)}<br>
    Maior: ${maior.toFixed(1)}<br>
    Menor: ${menor.toFixed(1)}
  `;
}
// TODO:
// 1. Pegar todas as notas da lista e adicionar 
// 2. Percorra a lista criada e converta para números float (use parseFloat())
// 3. Calcular: quantidade, média, maior nota, menor nota
// 4. Exibir as estatísticas na div com id "resultado-estatisticas"
// 5. Formato: "Quantidade: X", "Média: Y.Y", "Maior: Z.Z", "Menor: W.W"
// DICA: Use querySelectorAll("li") para pegar todas as notas da lista
// DICA: Use Math.max() e Math.min() para encontrar maior/menor
// DICA: Use innerHTML para adicionar HTML formatado dentro 
// da div com id "resultado-estatisticas"
// DICA: Use template strings para formatação dos resultados
// SEU CÓDIGO AQUI:







// ===========================================
// EVENT LISTENERS - NÃO MODIFICAR <<<<<<<<<<
// ===========================================
// Estes event listeners conectam os botões às funções
// NÃO ALTERE ESTA SEÇÃO <<<<<<<<<<

document.addEventListener("DOMContentLoaded", function () {
  // Exercício 1
  document
    .getElementById("btn-adicionar-nota")
    .addEventListener("click", adicionarNota);

  // Exercício 2
  document
    .getElementById("btn-calcular-media")
    .addEventListener("click", calcularMedia);

  // Exercício 3
  document
    .getElementById("btn-verificar-aprovacao")
    .addEventListener("click", verificarAprovacao);

  // Exercício 4
  document
    .getElementById("btn-gerar-estatisticas")
    .addEventListener("click", gerarEstatisticas);
});
