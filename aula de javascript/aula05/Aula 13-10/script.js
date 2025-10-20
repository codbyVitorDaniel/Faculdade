const itemForm = document.getElementById("itemForm");
const itemInput = document.getElementById("itemInput");
const itemList = document.getElementById("itemList");

itemForm.addEventListener("submit", (e) => {
  e.preventDefault(); // Prevê o recarregamento da página
  const item = itemInput.value.trim(); // Usar trim() para eliminar espaços extras

  if (item === "") return; // Não adicionar itens vazios

  const li = document.createElement("li");
  li.textContent = item;

  // Criar o botão de remover
  const removerButton = document.createElement("button");
  removerButton.textContent = "Remover";
  // Adiciona o botão dentro do <li>
  li.appendChild(removerButton);

  // Evento de remover o item
  removerButton.addEventListener("click", () => {
    li.remove(); // Remove o <li>
  });

  // Adiciona o <li> na lista
  itemList.appendChild(li);

  // Limpar o input
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

// Contar e listar os itens
const botaoContar = document.getElementById('contarItens');

botaoContar.addEventListener('click', () => {
  const todosOsItens = document.querySelectorAll('#itemList li');
  let contador = 0;

  todosOsItens.forEach((item, index) => {
    contador++;
    console.log(`Item ${index + 1}: ${item.textContent}`);
  });

  console.log(`Total de itens: ${contador}`);
});
