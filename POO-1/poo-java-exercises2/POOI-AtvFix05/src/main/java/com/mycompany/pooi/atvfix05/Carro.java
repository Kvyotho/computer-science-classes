package com.mycompany.pooi.atvfix05;

public class Carro {

    public String marca;
    public String modelo;
    public int ano;
    public double velocidade;
    
    
    public Carro(String marca, String modelo, int ano, double velocidade){
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = velocidade;
    }
    
    public void acelerar(double valor){
        if (valor >= 0){
        velocidade += valor;
    }
    }
    
    public void frear(double valor){
        if (valor >= 0){
        velocidade -= valor;
    }
    }
    
    public static void testeCorrida(Carro carro1, Carro carro2){
        if (carro1.velocidade > carro2.velocidade){
            System.out.printf("O primeiro carro ganhou a corrida.%n");
        }else if(carro2.velocidade > carro1.velocidade){
            System.out.printf("O segundo carro ganhou a corrida.%n");
        }else{
            System.out.printf("A corrida empatou.%n");
        }
        
    }
}
