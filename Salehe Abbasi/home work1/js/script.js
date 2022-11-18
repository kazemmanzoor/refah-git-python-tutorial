var input1 = document.getElementById("txt1");
var input2 = document.getElementById("txt2");
var button = document.getElementById("btn");



function Complex(real, imaginary) {
    this.real = 0;
    this.imaginary = 0;
    this.real = (typeof real === 'undefined') ? this.real : parseFloat(real);
    this.imaginary = (typeof imaginary === 'undefined') ? this.imaginary : parseFloat(imaginary);
  }
  Complex.transform = function(num) {
    var complex;
    complex = (num instanceof Complex) ? num : complex;
    complex = (typeof num === 'number') ? new Complex(num, 0) : num;
    return complex;
  };
  function display_complex(re, im) {
    // if(im === '0') return '' + re;
    // if(re === 0) return '' + im + 'i';
    // if(im < 0) return '' + re + im + 'i';
    // return '' + re + '+' + im + 'i';
    var a= "<pre><code>( "+(re>0?re:("- "+(re*-1)))+" ) + ( "+(im>0?(im):("- "+(im*-1)))+"i )</code></pre>";
    console.log(a);
    return a;
  }
  function complex_num_add(first, second) {
    var num1, num2;
    num1 = Complex.transform(first);
    num2 = Complex.transform(second);
    var real = num1.real + num2.real;
    var imaginary = num1.imaginary + num2.imaginary;
    return display_complex(real, imaginary);
  }

  function complex_num_minus(first, second) {
    var num1, num2;
    num1 = Complex.transform(first);
    num2 = Complex.transform(second);
    var real = num1.real - num2.real;
    var imaginary = num1.imaginary - num2.imaginary;
    return display_complex(real, imaginary);
  }

  function complex_num_multi(a , b , c , d) {
    var real =(a*c)-(b*d);
    var imaginary = (a*d)+(b*c);
    return display_complex(real, imaginary);
  }

  function complex_num_devide(a , b , c , d) {
    var real = ((a*c)-(b*d))/((c*c)+(d*d));
    var imaginary = (((a*d)+(b*c))/((c*c)+(d*d)));
    return display_complex(real, imaginary);
  }

  button.onclick = function(){
    let num1 = input1.value.split(",");
    let num2 = input2.value.split(",");

    let complex1 = new Complex(Number(num1[0]) ,Number( num1[1]));
    let complex2 = new Complex(Number(num2[0]) ,Number( num2[1]));


    document.querySelector(".answer1").innerHTML = complex_num_add(complex1 , complex2);
    document.querySelector(".answer2").innerHTML = complex_num_minus(complex1 , complex2);
    document.querySelector(".answer3").innerHTML = complex_num_multi(Number(num1[0]),Number(num1[1]),Number(num2[0]),Number(num2[1]));
    document.querySelector(".answer4").innerHTML = complex_num_devide(Number(num1[0]),Number(num1[1]),Number(num2[0]),Number(num2[1]));
    
}