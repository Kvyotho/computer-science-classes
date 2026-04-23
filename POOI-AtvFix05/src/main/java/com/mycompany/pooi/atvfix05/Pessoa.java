
package com.mycompany.pooi.atvfix05;


public class Pessoa {
    public String nome;
    public int idade;
    public String cidade;
    
    public Pessoa(String nome, int idade, String cidade){
        this.nome = nome;
        this.idade = idade;
        this.cidade = cidade;
    }
    
    public void exibirInfo(){
        System.out.printf("Nome: %s%nIdade: %d%nCidade: %s%n", nome, idade, cidade);
    }
    
}
