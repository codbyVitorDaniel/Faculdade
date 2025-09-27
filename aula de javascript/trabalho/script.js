const nomeInput = document.getElementById("nomeAluno");
const notaInput = document.getElementById("notaAluno");
const btnAdicionar = document.getElementById("btnAdicionar");
const listaUL = document.getElementById("listaAlunos");

let alunos = [];

function calcularSituacao(nota) {
    if (nota >= 7) {
        return "Aprovado";
    } else if (nota >= 4 && nota < 7) {
        return "Recuperação";
    } else {
        return "Reprovado";
    }
}

function atualizarLista() {
    listaUL.innerHTML = "";
    alunos.forEach(aluno => {
        const li = document.createElement("li");
        li.textContent = `${aluno.nome} - Nota: ${aluno.nota} - ${aluno.situacao}`;
        listaUL.appendChild(li);
    });
}

function adicionarAluno() {
    const nome = nomeInput.value.trim();
    const nota = Number(notaInput.value);

    if (nome === "" || isNaN(nota)) {
        alert("Preencha corretamente o nome e a nota do aluno.");
        return;
    }

    const aluno = {
        nome: nome,
        nota: nota,
        situacao: calcularSituacao(nota)
    };

    alunos.push(aluno);
    atualizarLista();
    nomeInput.value = "";
    notaInput.value = "";
}

btnAdicionar.addEventListener("click", adicionarAluno);
