package com.mycompany.pooi.atvfix05;

public class Personagem {

    private String nome;
    private int vida;
    private int forca;

    public Personagem(String nome, int vida, int forca) {
        this.nome = nome;
        this.vida = vida;
        this.forca = forca;
    }

    public String getNome() {
        return this.nome;
    }

    public int getVida() {
        return this.vida;
    }

    public int getForca() {
        return this.forca;
    }

    public void atacar(Personagem target) {
        target.vida -= this.forca;
        System.out.printf("%s atacou o %s com %d de dano.%n", nome, target.getNome(), forca);
    }

    public void exibirVida() {
        System.out.println(nome + " vida: " + vida);
    }
}
