const itemForm = document.querySelector('#itemForm');
const itemInput = document.querySelector('#itemInput');
const itemList = document.querySelector('#itemList');

const initialItems = ['Apple', 'Banana', 'Carrot']; // Exemplo de array com itens iniciais

// Renderizar os itens iniciais usando forEach
initialItems.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item;

  const removerItem = document.createElement('button');
  removerItem.textContent = 'Remover';

  li.appendChild(removerItem);

  removerItem.addEventListener("click", () => {
    li.remove();
  });

  itemList.appendChild(li);
});

itemForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const item = itemInput.value;

  if (!item) {
    alert("Por favor, insira um item");
    return;
  }

  const li = document.createElement('li');
  li.textContent = item;

  const removerItem = document.createElement('button');
  removerItem.textContent = 'Remover';

  li.appendChild(removerItem);

  removerItem.addEventListener("click", () => {
    li.remove();
  });

  itemList.appendChild(li);
  
  itemInput.value = '';
});
