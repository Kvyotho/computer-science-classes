package com.mycompany.pooi.atvfix05;

public class Retangulo {

    private int largura;
    private int altura;

    public Retangulo(int largura, int altura) {
        this.largura = largura;
        this.altura = altura;
    }

    public int calcArea() {
        return largura * altura;
    }

    public int calcPerimetro() {
        return (largura + altura) * 2;
    }

    public void compararRetangulo(Retangulo comparado) {
        if (this.calcArea() > comparado.calcArea()) {
            System.out.printf("O retangulo 1 tem maior área.%n");
        } else if (this.calcArea() < comparado.calcArea()) {
            System.out.printf("O retangulo 2 tem maior área.%n");
        } else {
            System.out.println("Os retangulos tem a mesma área.%n");
        }
    }
}
