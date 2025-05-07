// src/main.ts
function esPalindromo(valor) {
    var invertido = "";
    for (var i = valor.length - 1; i >= 0; i--) {
        invertido += valor[i];
    }
    return valor === invertido;
}
var input = document.getElementById("numero");
var btn = document.getElementById("verificar");
var resultado = document.getElementById("resultado");
btn.addEventListener("click", function () {
    var valor = input.value;
    var respuesta = esPalindromo(valor) ? "Sí es palíndromo" : "No es palíndromo";
    resultado.textContent = respuesta;
});
