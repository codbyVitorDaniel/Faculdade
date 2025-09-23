function soma(a, b) {
    return a + b;
}

console.log(soma(10, 10))

async function buscardados() {
    return "Dados Recebidos"
}

buscardados().then(console.log);

const dobro = (x) => x*2;
console.log(dobro(250))

function pegarDados() {
    return new Promise((resolve) =>{
        setTimeout(() =>  resolve ("Dados Recebidos! Depois de 200ms"), 2000);
    })
}
pegarDados().then((resposta) => console.log(resposta));