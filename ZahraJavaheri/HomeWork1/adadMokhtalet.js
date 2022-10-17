var real1 = prompt("قسمت حقیقی عدد اول را وارد کنید");
var imaginary1 = prompt("قسمت موهومی عدد اول را وارد کنید");
var real2 = prompt("قسمت حقیقی عدد دوم را وارد کنید");
var imaginary2 = prompt("قسمت موهومی عدد دوم را وارد کنید");

var real_answer = Number(real1) + Number(real2);
var imaginary_answer = Number(imaginary1) + Number(imaginary2);
var answer = real_answer + "+" + imaginary_answer + "i";
alert(answer);
