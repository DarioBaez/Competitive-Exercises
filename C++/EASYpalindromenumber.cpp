//Given an integer x, return true if x is a palindrome, and false otherwise.

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string solicitar_dato();
bool ValidarPalindromo(string palindromo);


int main(){


     string palindromo = solicitar_dato();

     bool esPalindromo = ValidarPalindromo(palindromo);

     if (esPalindromo == false){
          cout << "false";
     }
     else{
          cout << "true";
     }

     //cout << esPalindromo;

     return 0;
}


string solicitar_dato(){

     string numero;

     cout << "Introduce un numero: ";

     cin >> numero;

     return numero;
}


bool ValidarPalindromo(string palindromo){

     string omordnilaP;

     for (int i = 0; i < palindromo.length(); i++)
     {
          omordnilaP.append(1, palindromo[palindromo.length()-1-i]);
     }
     
     for (int i =0; i <palindromo.length(); i++){
          if (omordnilaP[i] != palindromo[i])
          {
               return false;
          }
     } 

     return true;
}