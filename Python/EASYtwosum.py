"""Dado un arreglo (array) de números enteros nums y un número entero target, 
devuelve los índices de los dos números que suman exactamente target.

Notas importantes:

Puedes asumir que siempre existirá exactamente una solución (no tienes que preocuparte de casos donde no haya respuesta).

No puedes usar el mismo elemento dos veces (por ejemplo, no puedes usar dos veces el mismo índice).

Puedes devolver los índices en cualquier orden (no importa si primero uno o el otro)."""
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):  # Importante: empezar desde i + 1 para no usar dos veces el mismo elemento
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # Por si acaso, aunque según el problema siempre hay solución

# Forma de pedir el arreglo:
def pedir_arreglo():
    nums = []

    while True:
        try:
            valor = int(input("Escribe un nuevo valor: "))
            nums.append(valor)
        except ValueError:
            target = int(input("Inserta tu target: "))
            break

    resultado = two_sum(nums, target)
    print("Indices encontrados:", resultado)

pedir_arreglo()
