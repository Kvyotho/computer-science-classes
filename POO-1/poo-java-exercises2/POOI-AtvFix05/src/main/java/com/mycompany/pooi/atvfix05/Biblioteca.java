package com.mycompany.pooi.atvfix05;

import java.util.ArrayList;

public class Biblioteca {

    private ArrayList<Livro> livros = new ArrayList<>();

    public void addLivro(Livro livro) {
        if (livro == null) {
            System.out.println("Esse livro não existe.");
        } else if (livros.contains(livro)) {
            System.out.printf("O livro %s já existe na biblioteca%n", livro.getTitulo());
        } else {
            livros.add(livro);
            System.out.printf("O livro %s foi adicionado com sucesso.%n", livro.getTitulo());
        }
    }

    public void removerLivro(Livro livro) {
        if (validarNC(livro)) {
            livros.remove(livro);
            System.out.printf("O livro %s foi removido com sucesso.%n", livro.getTitulo());
        }
    }

    public void emprestarLivro(Livro livro) {
        if (validarNC(livro) && livro.isDisponivel()) {
            livro.setDisponivel(false);
            System.out.printf("O livro %s foi emprestado com sucesso.%n", livro.getTitulo());
        } else {
            System.out.println("Erro ao emprestar livro.");
        }
    }

    public void devolverLivro(Livro livro) {
        if (!validarNC(livro)) {
            return;
        }
        if (!livro.isDisponivel()) {
            livro.setDisponivel(true);
            System.out.printf("O livro %s foi devolvido com sucesso.%n", livro.getTitulo());
        } else {
            System.out.printf("O livro %s já está disponível na biblioteca.%n", livro.getTitulo());
        }
    }

    public boolean validarNC(Livro livro) { // Valida Null, Contains
        if (livro == null) {
            System.out.printf("O livro não está existe na biblioteca.%n");
            return false;
        } else if (!livros.contains(livro)) {
            System.out.printf("O livro %s não está contido na biblioteca.%n", livro.getTitulo());
            return false;
        } else {
            return true;
        }
    }
}
