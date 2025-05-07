//Given an integer x, return true if x is a palindrome, and false otherwise.
using System;

class Program {
    static void Main(string[] args) {

    string Palindromo = SolicitarPalindromo();

    Console.WriteLine(Calculo_Palindromo(Palindromo));   



    }

    static string SolicitarPalindromo(){

        Console.WriteLine("Digite um número: ");
        string numero = Console.ReadLine();
        return numero;
    }


    static bool Calculo_Palindromo(string Palindromo){

        string omordnilaP = "";

        for (int  i = 0;  i < Palindromo.Length; i++)
        {
            omordnilaP += Palindromo[Palindromo.Length - i - 1];
        }
        for  (int i = 0; i < Palindromo.Length; i++)
        {
            if (omordnilaP[i] != Palindromo[i]){

                return false;

            }
        }       
        return true;
    }
}