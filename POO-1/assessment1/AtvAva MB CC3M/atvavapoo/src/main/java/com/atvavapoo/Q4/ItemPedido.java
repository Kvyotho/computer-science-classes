package com.atvavapoo.Q4;

public class ItemPedido {
    private String produto;
    private int quantidade;
    private double preco;

    public ItemPedido(String produto, int quantidade, double preco){
        this.produto = produto;
        this.quantidade = quantidade;
        this.preco = preco;
    }

    public double getSubtotal(){
        return quantidade * preco;
    }
    
}
