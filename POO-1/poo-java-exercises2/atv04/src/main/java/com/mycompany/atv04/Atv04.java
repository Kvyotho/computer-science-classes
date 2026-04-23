package com.mycompany.atv04;

public class Atv04 {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        Pessoa p1 = new Pessoa();
        p1.info();
        p1.mediaIdades();
        p1.maiorIdade();
        p1.menorIdade();
        p1.qntIdade();
        
        PopulacaoBaratas pb1 = new PopulacaoBaratas();
        pb1.getNumeroBaratas();
        pb1.aumentaBaratas();
        pb1.getNumeroBaratas();
        pb1.spray();
        pb1.getNumeroBaratas();

        Cozinha c1 = new Cozinha();
        c1.simular();
    }
}
