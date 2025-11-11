let log = new log(document.querySelector(".Log"));
let char = new Knight('Meliodas');
let Monster = new LittleMonster();


const stage = new Stage(
    char,
    Monster,
    document.querySelector('#char'),
    document.querySelector('#monster'),
    log
);


stage.start();
