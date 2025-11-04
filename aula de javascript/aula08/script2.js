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

function newPerson(name, age) {
    let p1 = new Person(name);
    p1.age = age;
    return p1
}
console.log(`Meus personagens tem: ${pessoa1.hands}`)