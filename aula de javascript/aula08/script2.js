class Person {
    constructor(name) {
        this.name = name
    }
}

class Student extends Person{
    constructor(name, id) {
        super(name)
        this.id = id
    }
}