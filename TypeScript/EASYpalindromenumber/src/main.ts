// src/main.ts
function esPalindromo(valor: string): boolean {
     let invertido = "";
     for (let i = valor.length - 1; i >= 0; i--) {
         invertido += valor[i];
     }
     return valor === invertido;
 }
 
 const input = document.getElementById("numero") as HTMLInputElement;
 const btn = document.getElementById("verificar")!;
 const resultado = document.getElementById("resultado")!;
 
 btn.addEventListener("click", () => {
     const valor = input.value;
     const respuesta = esPalindromo(valor) ? "Sí es palíndromo" : "No es palíndromo";
     resultado.textContent = respuesta;
 });
 