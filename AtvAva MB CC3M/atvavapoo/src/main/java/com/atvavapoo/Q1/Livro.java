package com.atvavapoo.Q1;

public class Livro {
    private String titulo;
    private String autor;
    private String ano;
    private boolean disponivel;

    public Livro(String titulo, String autor, String ano, boolean disponivel){
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true;
    }

    public String getTitulo(){
        return this.titulo;
    }
    
    public boolean isDisponivel(){
        return this.disponivel;
    }

    public void setDisponivel(boolean a){
        this.disponivel = a;
    }
}

