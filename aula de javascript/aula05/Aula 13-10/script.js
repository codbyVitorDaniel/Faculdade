// Arquivo JavaScript para os alunos implementarem
// Sugestões de funcionalidades para implementar:
// 1. Capturar o evento de submit do formulário
// 2. Pegar o valor do input
// 3. Criar um elemento <li> com o valor digitado
// 4. Adicionar o <li> na lista (ul#itemList)
// 5. Limpar o input após adicionar
// 6. (Extra) Adicionar botão de remover em cada item da lista

const itemForm = document.getElementById("itemForm");
const itemInput = document.getElementById("itemInput");
const itemList = document.getElementById("itemList");
// ou itemForm = document.querySelector("#itemForm");
// ou itemInput = document.querySelector("#itemInput");
// ou itemList = document.querySelector("#itemList");

itemForm.addEventListener("submit", (e) => {
  e.preventDefault(); //previne o recarregamento da pagina quando o formulario é enviado
  const item = itemInput.value;
  const li = document.createElement("li");

  li.textContent = item;

  //--------------------------------
  //adicionando botao remover
  //jeito errado
  // const adicionarButton = document.querySelector("ul"); //seleciona a lista
  // adicionarButton.before("<button>Remover</button>"); //adiciona o botao antes da lista

  // const newButton = document.createElement("button"); //cria o botao
  // newButton.innerText = "Botao"; //adiciona o texto ao botao
  // adicionarButton.after(newButton); //adiciona o botao depois da lista

  // -----------------------------
  //jeito certo
  const removerButton = document.createElement("button");
  removerButton.textContent = "Remover";
  // Adiciona o botão DENTRO do <li>
  li.appendChild(removerButton);
  //li.preped(removerButton); //adiciona o botao antes do texto do item

  // Adiciona o evento de clique no botão para remover o item
  removerButton.addEventListener("click", () => {
    // Remove o <li> pai do botão
    li.remove();
  });
  // //-----------------------------

  // Adiciona o <li> completo na lista
  itemList.appendChild(li);

  // Limpa o input
  itemInput.value = "";
});

function clicou() {
  const botao = document.querySelector(".botao");

  if (itemInput.getAttribute("type") === "text") {
    itemInput.setAttribute("type", "password");
    botao.innerText = "Mostrar Item";
  } else {
    itemInput.setAttribute("type", "text");
    botao.innerText = "Ocultar Item";
  }
}

// ========================================
// EXEMPLO DE USO DO forEach
// ========================================
// O forEach é um método que percorre cada elemento de um array ou lista
// Ele executa uma função para cada item encontrado

// 1. Selecionar o botão que foi criado no HTML

//ou const botaoContar = document.querySelector("#contarItens");

// 2. Adicionar um evento de clique no botão

  // 3. Pegar todos os elementos <li> que estão dentro da lista
  // querySelectorAll retorna uma NodeList (parecido com um array)
  

  // 4. Criar uma variável para contar os itens


  // 5. Usar o forEach para percorrer cada item da lista
  // forEach recebe uma função que será executada para cada item
  // O parâmetro 'item' representa cada elemento <li> da lista
  // O parâmetro 'index' representa a posição do item (0, 1, 2, 3...)
  
    // 6. Para cada item, incrementar o contador
    

    // 7. Mostrar no console cada item e sua posição
   

  // 8. Após percorrer todos os itens, mostrar a quantidade total
  // Usamos um alert para exibir a mensagem na tela
  

  // 9. Também mostramos no console
 

// RESUMO DO forEach:
// forEach(função) - executa a função para cada elemento
// Sintaxe: array.forEach((elemento, indice) => { ... })
// - elemento: o item atual sendo percorrido
// - indice: a posição do item (opcional)



// Modo 1

// Modo 2

//Trabalhando com classes no DOM





