const fs = require('fs');
var ddc = 100;
function f1(id) {
    id++;
    fs.readFile('./package.json', (err, data) => {
        console.log(id);
        let dd = 10;
        setTimeout(function() {
            console.log(id++, dd);
            fs.readFile(__filename, () => {
                console.log(id, dd);
            });
        }, 1000)
    })
}
f1(111)