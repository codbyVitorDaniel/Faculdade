const nome = document.getElementById("nomeAluno");
const nota = document.getElementById("notaAluno");
const btn = document.getElementById("btnAdicionar"); 
const listaUL = document.getElementById("listaAlunos");
let lista = [];

btn.addEventListener("click", function () {
    const nomeAluno = nome.value.trim();
    const notaAluno = Number(nota.value);

    if (nomeAluno === "" || isNaN(notaAluno)) {
        alert("Preencha o nome e a nota corretamente!");
        return;
    }

    let situacao = "";
    if (notaAluno >= 7) {
        situacao = "Aprovado";
    } else if (notaAluno >= 4 && notaAluno < 7) {
        situacao = "Recuperação";
    } else {
        situacao = "Reprovado";
    }

    lista.push({ nome: nomeAluno, nota: notaAluno, situacao: situacao });

    const li = document.createElement("li");
    li.textContent = `${nomeAluno} - ${situacao}`;
    listaUL.appendChild(li);
    nome.value = "";
    nota.value = "";
});

const teste = document.getElementById("teste")
