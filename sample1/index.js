'use strict';
const Braj = require("./braj");
let bk1 = new Braj(1, "TestProj");
// console.log(bk1.id);
// console.log(bk1.proj);

// console.log(bk1.workingOn);
// bk1.workingOn = "Testing classes";
// // bk1.sayhello();
// console.log(bk1.workingOn);
// Braj.sayhello();
// console.log(bk1.displayName);
// console.log(Braj.displayName);

class BrajTester extends Braj {
    #testingrightnow=false;
    constructor(child, id, proj) {
        super(id, proj);
        this.child = child;
        this.testing = [];
    }
    test(work) {
        this.#testingrightnow = true;
        this.testing.push(work);
    }
    get testingOn() {
        return this.testing;
    }
    get testingnow() {
        return this.#testingrightnow;
    }

}

const bkt1 = new BrajTester("testpart", 1, "TestProj");
console.log(bkt1.id);
bkt1.workingOn = "Test Project part 1";
console.log(bkt1.workingOn);
console.log(BrajTester.displayName)
Braj.sayhello();
BrajTester.sayhello();
console.log(bkt1.id);
console.log(bkt1.testingnow);
bkt1.test("test proj 2")
console.log(bkt1.testingnow);

console.log(bkt1);  

