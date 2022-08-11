'use strict'
class Braj {
    static displayName = "Braj";
    constructor(id, proj) {
        this.id = id;
        this.proj = proj;
        this.working = [];
    }
    static sayhello() {
        console.log("Hello from Braj");
        this.id =3;
        console.log(this, this.id, this.proj);
    }
    get workingOn() {
        console.log("In this working getter");
        return this.working;
    }
    set workingOn(projPart) {
        this.working.push(projPart);
    }
}
module.exports = Braj;