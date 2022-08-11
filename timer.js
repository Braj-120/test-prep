const fs = require("fs").promises;
let i =0;
async function longfun() {
    console.log("Entering", ++i);
    let j = 100;
    // let j =1;
    // for (let i =0; i< 10000000000; i++) {
    //     j++
    // }
    // console.log(j);
    // fs.readFile("D:\\overlord\\Innocent_Witches-0-9-beta-pc.zip", (err, data) => {
    //     console.log(data, err);
    //     console.log("Inside the file read", j++, i);
    // });
    await fs.readFile("D:\\overlord\\The_Lewd_Knight-0.7.rar")
    console.log("Inside the file read", j++, i);

}
let timer = setInterval(longfun, 100)

// setInterval(async () => {
//     await fetch("https://www.google.com/") 
//     console.log("Braj", ++i)
// }, 10);
