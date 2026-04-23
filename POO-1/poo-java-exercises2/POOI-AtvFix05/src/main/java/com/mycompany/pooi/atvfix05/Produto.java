package com.mycompany.pooi.atvfix05;

import java.util.ArrayList;

public class Produto {

    private String nome;
    private int preco;
    private int quantidade;
    static ArrayList<Produto> estoqueGeral = new ArrayList<>();

    public Produto(String nome, int preco, int quantidade) {
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
        estoqueGeral.add(this);
    }

    public String getNome(){
        return this.nome;
    }

    public double totalProduto() {
        return preco * quantidade;
    }

    public static double totalEstoque() {
        double somatotal = 0;
        for (Produto p : estoqueGeral) {
            somatotal += p.preco * p.quantidade;
        }
        return somatotal;
    }
}
