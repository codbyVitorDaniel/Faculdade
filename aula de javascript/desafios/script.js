// Arquivo JavaScript para os alunos implementarem
// SugestÃµes de funcionalidades para implementar:
// 1. Capturar o evento de submit do formulÃ¡rio
// 2. Pegar o valor do input
// 3. Criar um elemento <li> com o valor digitado
// 4. Adicionar o <li> na lista (ul#itemList)
// 5. Limpar o input apÃ³s adicionar
// 6. (Extra) Adicionar botÃ£o de remover em cada item da lista

const itemForm = document.getElementById('itemForm')
const itemInput = document.getElementById('itemInput')
const itemList = document.getElementById('itemList')
// ou itemForm = document.querySelector("#itemForm");
// ou itemInput = document.querySelector("#itemInput");
// ou itemList = document.querySelector("#itemList");

itemForm.addEventListener('submit', (e) => {
  e.preventDefault() //previne o recarregamento da pagina quando o formulario Ã© enviado
  const item = itemInput.value
  const li = document.createElement('li')

  li.textContent = item

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
  const removerButton = document.createElement('button')
  removerButton.textContent = 'Remover'
  // Adiciona o botÃ£o DENTRO do <li>
  li.appendChild(removerButton)
  //li.preped(removerButton); //adiciona o botao antes do texto do item

  // Adiciona o evento de clique no botÃ£o para remover o item
  removerButton.addEventListener('click', () => {
    // Remove o <li> pai do botÃ£o
    li.remove()
  })
  // //-----------------------------

  // Adiciona o <li> completo na lista
  itemList.appendChild(li)

  // Limpa o input
  itemInput.value = ''
})

function clicou() {
  const botao = document.querySelector('.botao')

  if (itemInput.getAttribute('type') === 'text') {
    itemInput.setAttribute('type', 'password')
    botao.innerText = 'Mostrar Item'
  } else {
    itemInput.setAttribute('type', 'text')
    botao.innerText = 'Ocultar Item'
  }
}

// ========================================
// EXEMPLO DE USO DO forEach
// ========================================
// O forEach Ã© um mÃ©todo que percorre cada elemento de um array ou lista
// Ele executa uma funÃ§Ã£o para cada item encontrado

// 1. Selecionar o botÃ£o que foi criado no HTML
const botaoContar = document.getElementById('contarItens')

//ou const botaoContar = document.querySelector("#contarItens");

// 2. Adicionar um evento de clique no botÃ£o
botaoContar.addEventListener('click', () => {
  const todosOsItens = document.querySelectorAll('#itemList li')
  let contador = 0

  todosOsItens.forEach((item, index) => {
    contador++
    console.log(`Item ${index + 1}: ${item.textContent}`)
  })

  alert(`Total de itens na Lista: ${contador}`)
  console.log(`==== Total de Itens: ${contador}`)
})
// RESUMO DO forEach:
// forEach(funÃ§Ã£o) - executa a funÃ§Ã£o para cada elemento
// Sintaxe: array.forEach((elemento, indice) => { ... })
// - elemento: o item atual sendo percorrido
// - indice: a posiÃ§Ã£o do item (opcional)

// Modo 1
function clicouMudaCor() {
  const listaItens = document.querySelectorAll('#itemList li')

  listaItens.forEach((item) => {
    item.style.backgroundColor = '#a4aa02ff'
    item.style.color = '#ffffffff'
    item.style.fontSize = '50px'
  })
}

// Modo 2
const botaoMudarCor = document.getElementById('mudarCor2')
botaoMudarCor.addEventListener("click", () => {
  const todosOsItens = document.querySelectorAll('#itemList li');
  const botaoRemover = document.querySelectorAll("#itemList li button")


  todosOsItens.forEach((item, index) => {
    item.style.color ="#ffff"
    item.style.fontSize = "50px"

    if(index % 2 === 0) {
      item.style.backgroundColor = "#989898ff" // se for par esta cor
      botaoRemover[index].style.backgroundColor = "#009f05ff"
      botaoRemover[index].style.color = "#ffffffff"
    } else {
      item.style.backgroundColor = "#404040ff" // se for impar esta cor
      botaoRemover[index].style.backgroundColor = '#f9e573ff'
      botaoRemover[index].style.color = '#4a4a4aff'
    }
  });
});

//Trabalhando com classes no DOM
function clicouClasses(){
  const mudarClasses = document.querySelector('#botaoClasses')

  // if (mudarClasses.classList.contains("Vermelho")){
  //   mudarClasses.classList.add("Azul")
  //   mudarClasses.classList.remove("Vermelho")
  // } else {
  //   mudarClasses.classList.add("Vermelho")
  //   mudarClasses.classList.remove("Azul")
  // }

  // mudarClasses.classList.toggle("Azul")

  if (mudarClasses.classList.contains("Azul")){
    mudarClasses.classList.replace("Azul", "Vermelho")
  } else {
    mudarClasses.classList.replace("Vermelho", "Azul")
  }
}