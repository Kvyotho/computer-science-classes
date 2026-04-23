package com.mycompany.pooi.atvfix05;

import java.util.ArrayList;

public class Aluno {

    private String nome;
    private ArrayList<Double> notas = new ArrayList<>();

    public Aluno(String nome, double nota1, double nota2, double nota3) {
        this.nome = nome;
        notas.add(nota1);
        notas.add(nota2);
        notas.add(nota3);
    }

    public void calcMedia() {
        double soma = 0;
        for (int i = 0; i < notas.size(); i++) {
            soma += notas.get(i);
        }
        double media = soma / notas.size();
        if (media >= 7) {
            System.out.printf("O aluno %s passou de ano.%n", nome);
        } else {
            System.out.printf("O aluno %s não passou de ano.%n", nome);
        }
    }
}
