// primeiro 

// //function nomeCompleto(nome, sobrenome){ 
//     return( `${nome} ${sobrenome}`)
// };

// let nome = nomeCompleto('Vitor', 'Daniel');

// console.log(nome)

// segundo

// function maiorIdade(idade){
//     if(idade >= 18){
//         return true
//     }else{
//         return false
//     }
// }

// let idade = 14;
// let verificacao = maiorIdade(idade);

// if (verificacao){
//     console.log("Voce e maior de Idade")
// }else{
//     console.log("Voce e menor de idade!")
// }

// function calcular(x,y){
//     let calc = (y/x) * 100;
//     return calc;
// }
// let custodoproduto = 40 
// let desconto = 10
// let calculo = calcular(custodoproduto,desconto)
// console.log(`Um desconto de R$: ${desconto}, representa ${calculo}% do valor do produto, que custa R$ ${custodoproduto}`)

//exercicio 

// let profissional = "Fiscal"
// console.log(`A sua profissao e: ${profissional}`)

// switch (profissional) {
//     case `Fiscal`:
//         console.log(`Sua camisa sera verde`)
//         break;
//     case `policial`:
//         console.log(`Sua camisa sera azul`)
//         break;
//     case `Bombeiro`:
//         console.log(`Sua camisa sera vermelho`)
//         break;
//     default:
//         console.log(`Sua camisa sera preta`)
//         break;
//}

//exercicio 

// function calcularImovel(metragem, quartos) {
//     let m2 = 3000;
//     let preco = 0;

//     switch (quartos) {
//         case 1:
//             preco = metragem * m2 * 1;
//             break;
//         case 2:
//             preco = metragem * m2 * 1.2;
//             break;
//         case 3:
//             preco = metragem * m2 * 1.5;
//             break;
//         default:
//             preco = metragem * m2;
//     }

//     return preco;
// }

// let metragem = 123;
// let quartos = 4;
// let preco = calcularImovel(metragem, quartos);
// console.log(`A casa custa R$ ${preco}`);

//exercicio 

function validar(usuario, senha) {
    if (usuario === "admin" && senha === "123"){
        return true
    }else{
        return false
    }
};
let usuario = "Vitor"
let senha = "123456"
let validacao = validar(usuario,senha)
if (validacao){
    console.log("Acesso concedido")
}else{
    console.log("acesso negado")
}