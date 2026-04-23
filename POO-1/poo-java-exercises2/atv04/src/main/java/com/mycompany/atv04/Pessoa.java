package com.mycompany.atv04;

import java.util.Scanner;

public class Pessoa {

    Scanner scanner = new Scanner(System.in);
    String[] nomes = new String[5];
    int[] idades = new int[5];
    

//Solicita 5 nomes e 5 idades ao usuário
public void info() { 
        for (int i = 0; i < 5; i++) {
            System.out.println("Digite o " + (i + 1) + " nome: ");
            nomes[i] = scanner.nextLine();
            System.out.println("Digite a " + (i + 1) + " idade: ");
            idades[i] = scanner.nextInt();
            scanner.nextLine(); //buffer cleaning
        }
}

//Calcula a média das idades
public void mediaIdades(){
    double soma = 0;
    for (int i = 0; i < idades.length; i++){
        soma += idades[i];
    }
    System.out.println("A média das idades é: "+ (soma/idades.length));
}

public void maiorIdade(){
    int maior = 0;
    for (int i = 0; i < idades.length; i++){
        if (idades[i] > maior){
            maior = idades[i];
        }
    }
    System.out.println("A maior idade é: "+maior);
}
public void menorIdade(){
    int menor = idades[0];
    for (int i = 0; i < idades.length; i++){
        if (idades[i] < menor){
            menor = idades[i];
        }
    }
    System.out.println("A menor idade é: " +menor);
}

//Calcula a quantidade de maiores de idade
public void qntIdade(){
    int maiorDeIdade = 18;
    int qnt = 0;
    for (int i = 0; i < idades.length; i++){
        if (idades[i] >= maiorDeIdade){
            qnt++;
        }
    }
    System.out.println("A quantidade de maiores de idade é: "+qnt);
}

}
