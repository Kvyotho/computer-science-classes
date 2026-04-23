package com.mycompany.listadiagramas;

public class Produto {

    int codigo;
    int fornecedor_codigo;
    String nome;
    double valor;
    int estoque;

    public Produto(int codigo, int fornecedor_codigo, String nome, double valor, int estoque) {
        this.codigo = codigo;
        this.fornecedor_codigo = fornecedor_codigo;
        this.nome = nome;
        this.valor = valor;
        this.estoque = estoque;
    }

    public void cadastrar(Produto produto) {

    }

    public void editar(Produto produto) {

    }

    public void excluirEstoque(int quantidade) {

    }
}
