#Given an integer x, return true if x is a palindrome, and false otherwise.

def Input():

     x_string = str(input("Ingresa un numero: "))
     print(Calculo_Palindromo(x_string))

def Calculo_Palindromo(x_string):
     palindrome = True;

     x_string_invertido = x_string[::-1]


     for I in range(len(x_string)):
          
          if x_string[I] != x_string_invertido[I]:
               
               palindrome = False;
               return palindrome

     return palindrome
     

Input()
