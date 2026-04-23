package com.atvavapoo.Q1;

import java.util.ArrayList;

public class Biblioteca {

    ArrayList<Livro> livros = new ArrayList<>();

    public void adicionarLivro(Livro livro) {
        if (livros.contains(livro)) {
            livros.add(livro);
        }
    }

    public Livro buscarLivroPorTitulo(String titulo) {
        for (Livro l : livros) {
            if (l.getTitulo().equalsIgnoreCase(titulo)) {
                return l;
            }
        }
        return null;
    }

    public void emprestarLivro(String titulo) throws LivroIndisponivelException {
        Livro livro = buscarLivroPorTitulo(titulo);
        if (livro == null)
            throw new LivroIndisponivelException("O Livro não foi encontrado");
        if (livro.isDisponivel() == false)
            throw new LivroIndisponivelException("O livro não está disponível");
        livro.setDisponivel(false);
    }

    public void devolverLivro(String titulo){
        Livro livro = buscarLivroPorTitulo(titulo);
        if (livro != null){
            livro.setDisponivel(true);
        }
    }
}
