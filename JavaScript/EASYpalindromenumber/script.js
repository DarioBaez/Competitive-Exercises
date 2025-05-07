function comprobarPalindromo() {
     const numero = document.getElementById('numero').value;
     const resultado = document.getElementById('resultado');
 
     // Validar si el input es un número
     if (isNaN(numero) || numero === "") {
         resultado.textContent = "Por favor, ingresa un número válido.";
         return;
     }
 
     // Verificar si el número es un palíndromo
     const numeroInvertido = numero.split('').reverse().join('');
     if (numero === numeroInvertido) {
         resultado.textContent = `El número ${numero} es un palíndromo.`;
     } else {
         resultado.textContent = `El número ${numero} no es un palíndromo.`;
     }
 }
 