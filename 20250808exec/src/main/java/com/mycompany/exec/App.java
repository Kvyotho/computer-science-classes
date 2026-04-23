package com.mycompany.exec;
import java.util.Scanner;
public class App {

    public static void main(String[] args) {
        
         Scanner scanner = new Scanner(System.in);
        //Exec 01
        
        System.out.println("Digite a primeira nota: ");
        float nota1 = scanner.nextFloat();
        System.out.println("Digite a segunda nota: ");
        float nota2 = scanner.nextFloat();
        System.out.println("Digite a terceira nota: ");
        float nota3 = scanner.nextFloat();
        float avgnotas = (nota1 + nota2+ nota3) / 3; //média das 3 notas
        System.out.println("A média das notas é: " + avgnotas);
        
        
        //Exec 02
      
        System.out.println("Digite a temperatura em ºC: ");
        float tempcelsius = scanner.nextFloat();
        float CtF = (tempcelsius * 9/5) + 32; //Celsius to Fahrenheit
        System.out.println("A temperatura em ºF é: " + CtF);
        
        
        //Exec 03
        
        System.out.println("Digite seu nome:");
        String nome = scanner.next();
        System.out.println("Digite seu sobrenome:");
        String sobrenome = scanner.next();
        System.out.printf("O seu nome completo é: %s %s \n", nome, sobrenome); //1 utilizando printf  
        System.out.println("O seu nome completo é: " + nome +" " +sobrenome); //2 utilizando println
        
        
        //Exec 04

        System.out.println("Digite uma frase: ");
        String frase = scanner.next();
        System.out.println("A frase digitada contem: " + frase.length() + " caracteres");
        
        
        //Exec 05
        final float pi = (float) 3.14;
        System.out.println("Digite o raio do circulo: ");
        float raio = scanner.nextFloat();
        System.out.println("A área do circulo é: " +pi * (raio*raio));
        
        scanner.close();   
    }
}
