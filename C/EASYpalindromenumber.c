//Given an integer x, return true if x is a palindrome, and false otherwise.
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


void Solicitar_input(char palindromo[50]);

bool CalculoPalindromo(char resultado[50]);

int main(){
     
     char palindromo[50];
     
     Solicitar_input(palindromo);

     bool esPalindromo = CalculoPalindromo(palindromo);

     if (esPalindromo == 1){
          printf("true");
     }else{
          printf("false");
     }

     //printf("%d\n", esPalindromo);

     return 0;
}

void Solicitar_input(char palindromo[50]){

     printf("Introduce un numero: ");

     scanf("%s", palindromo);
}


bool CalculoPalindromo(char resultado[50]){

     int lenResultado = strlen(resultado);

     for (int i = 0; i < lenResultado / 2; i++)
     {
          if(resultado[i] != resultado[lenResultado-i-1]){
               return false;
          }
     }
     
     return true;
}

