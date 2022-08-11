
var num = [9,9,9];
var toadd = 1;
function add(num, toadd) {
  let lengthofarr = num.length;
  let newArr = [];
  let val = num[lengthofarr-1] + toAdd;
  if (num[lengthofarr-1] + toadd > 10) {
    newArr = Array.from(num);
    num.pop();
    while(val > 0) {
      let s = val%10;
      newArr.push(s);
      val = Math.floor(val / 10);
    }
  } else {
    newArr[lengthofarr-1] = val;
  }
  console.log(newArr);
}


add(num, toadd)





























