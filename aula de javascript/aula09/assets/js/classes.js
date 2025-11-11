class Character {
    _life = 1;
    maxLife = 1;
    attack = 0;
    defense = 0;

    constructor(name) {
        this.name = name;
    }

    get life() {
        return this._life;
    }

    set life(newLife) {
        this._life = newLife < 0 ? 0 : newLife;
    }
}

class Knight extends Character {
    constructor(name) {
        super(name);
        this.life = 100;
        this.attack = 10;
        this.defense = 8;
        this.maxLife = this.life;
    }
}

class Sorcerer extends Character {
    constructor(name) {
        super(name);
        this.life = 80;
        this.attack = 15;
        this.defense = 3;
        this.maxLife = this.life;
    }
}

class LittleMonster extends Character {
    constructor() {
        super('LittleMonster');
        this.life = 40;
        this.attack = 4;
        this.defense = 4;
        this.maxLife = this.life;
    }
}

class BigMonster extends Character {
    constructor() {
        super('Big Monster');
        this.attack = 120;
        this.defense = 16;
        this.life = 200;
        this.maxLife = this.life;
    }
}

class Stage {
    constructor(fighter1, fighter2, fighter1EL, fighter2EL, logObject) {
        this.fighter1 = fighter1;
        this.fighter2 = fighter2;
        this.fighter1EL = fighter1EL;
        this.fighter2EL = fighter2EL;
        this.logObject = logObject
    }

    start() {
        this.update();
        this.fighter1EL.querySelector('.attackerButton');
        addEventListener("click", () => {
            this.doAttack(this.fighter1, this.fighter2)
        });

        addEventListener("click", () => {
            this.doAttack(this.fighter2, this.fighter1)
        });

        doAttack(attacking, attacked){
            // verificaçao basica
            if (attacking.life <= 0) {
                alert('Voce nao tem vida')
            }
            let attackFactor = (Math.random() * 2).toFixed(2)
            let defenseFactor = (Math.random() * 2).toFixed(2)

            let actualAttack = attacking.attack * attackFactor
            let actualDefense = attacked.defense * defenseFactor
            if (actualAttack > actualDefense) {
                attacked.life -= actualAttack;
            }
            console.log(`${attacking.name} causou ${actualAttack.toFixed(2)} de dano em ${attacked.name}`)
        } else {
            console.log(`${attacked.name} conseguiu defender o ataque de ${attacked.}`)
        }
    }

    update() {
        this.fighter1EL.querySelector('.name').innerHTML = `${this.fighter1.name} - ${this.fighter1.life} HP`;
        let f1pct = (this.fighter1.life / this.fighter1.maxLife) * 100;
        this.fighter1EL.querySelector(".bar").style.width = `${f1pct}%`;

        this.fighter2EL.querySelector('.name').innerHTML = `${this.fighter2.name} - ${this.fighter2.life} HP`;
        let f2pct = (this.fighter2.life / this.fighter2.maxLife) * 100;
        this.fighter2EL.querySelector(".bar").style.width = `${f2pct}%`;
    }

    attack() {

        let damage1 = Math.max(0, this.fighter1.attack - this.fighter2.defense);
        let damage2 = Math.max(0, this.fighter2.attack - this.fighter1.defense);


        this.fighter1.life -= damage2;
        this.fighter2.life -= damage1;


        this.update();
    }
}

class Log {
    list = []

    constructor(listEl){
        this.listEl = listEl;
    }

    addMenssage(msg){
        this.list.push(msg)
        this.render()
    }

    render(){
        this.listEl.innerHTML = "";

        for (let i in this.list){
            this.listEl.innerHTML += `<li>${this.list[i]}<\li>`;
        }
    }
}