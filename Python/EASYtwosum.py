"""Dado un arreglo (array) de números enteros nums y un número entero target, 
devuelve los índices de los dos números que suman exactamente target.

Notas importantes:

Puedes asumir que siempre existirá exactamente una solución (no tienes que preocuparte de casos donde no haya respuesta).

No puedes usar el mismo elemento dos veces (por ejemplo, no puedes usar dos veces el mismo índice).

Puedes devolver los índices en cualquier orden (no importa si primero uno o el otro)."""

def ArrayOrderer(Array, T):

     n = len(Array);
     for I in range(n):

          for j in range(0, n - I - 1):

               if Array[j] > Array[j + 1]:
                    Array[j], Array[j + 1] = Array[j + 1], Array[j]
     
     Suma = 0
     IndexList = []
     

     for I in range(len(Array)):
               
          Suma  += Array[I]
          IndexList.append(Array.index(Array[I]))

          if T == Suma:
               break
          elif T < Suma:
               
               break
        
     print(Array)
     print(T)
     print(IndexList)


def PedirArreglo():
     
     Array = []

     while True:

          try:
               Resultado = int(input("Write your new value: "))
               Array.append(Resultado)

          except ValueError:

               
               target = int(input("Insert your target: "))
               break

     ArrayOrderer(Array, target);

     

PedirArreglo()




"""Array = [3,2,4,5,1,23,123,12,3,4,44,12,452,5,3]
print(ArrayOrderer(Array))"""
