class Person {
    passos = 0;
    constructor(fistName, lastName) {
        this.name = fistName
        this.age = lastName
    }

    get fullName(){
        return `${this.fistName} ${this.lastName}`
    }

    get idade(){
        return this._idade
    }
    set idade(newAge){

        if (typeof newAge === 'number'){
            this._idade = newAge;
        } else {
            console.log('Idade so aceita numeros.')
        }
    }
    takeStep(){
        this.passos++;
    }
}

let pessoa1 = new Person('Joao', 'Carros')
pessoa1.idade = 30;

pessoa1.takeStep()
pessoa1.takeStep()
pessoa1.takeStep()
pessoa1.takeStep()

console.log(`Personagem 1: ${pessoa1.fullName} tem ${pessoa1.age} de idade`)
console.log(`Personagem 1: ${pessoa1.passos} passos`)
