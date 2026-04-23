package com.mycompany.listadiagramas;

public class Fornecedor {

    int codigo;
    String nome;
    String endereco;
    String bairro;
    String cidade;
    String uf;
    int cep;
    int telefone;

    public Fornecedor(int codigo, String nome, String endereco, String bairro, String cidade, String uf, int cep, int telefone) {
        this.codigo = codigo;
        this.nome = nome;
        this.endereco = endereco;
        this.bairro = bairro;
        this.cidade = cidade;
        this.uf = uf;
        this.cep = cep;
        this.telefone = telefone;
    }

    public void cadastrar(Fornecedor fornecedor) {
        //arraylist fornecedores, check if already exists, otherwise add
    }

    public void editar(Fornecedor fornecedor) {
        //remove/edit fornecedores from said arraylist above
    }
}
