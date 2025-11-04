class Person1 {
    static hands = 2;

    age = 0;
    constructor(name) {
        this.name = name
    }
    sayHi(){
        console.log(`${this.name} esta dizendo?`)
    }
}

class Student extends Person1{
    constructor(name, id) {
        super(name)
        this.id = id
    }
}

pessoa1 = new Student('Joaquim')
pessoa1 = new Student('OI')
pessoa1 = new Student('GOl')
pessoa1.age = 20
console.log(`Meus personagens tem: ${pessoa1.hands}`)