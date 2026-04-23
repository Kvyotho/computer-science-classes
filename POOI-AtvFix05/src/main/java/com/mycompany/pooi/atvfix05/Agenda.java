package com.mycompany.pooi.atvfix05;

import java.util.ArrayList;

public class Agenda {

    private static ArrayList<Contato> agenda = new ArrayList<>();

    public void addContato(Contato contato) {
        if (contato == null) {
            System.out.println("Esse contato não existe.");
        } else if (agenda.contains(contato)) {
            System.out.printf("O contato %s já existe na agenda%n", contato.getNome());
        } else {
            agenda.add(contato);
            System.out.printf("O contato %s foi adicionado com sucesso.%n", contato.getNome());
        }
    }

    public void removeContato(Contato contato) {
        if (validarNC(contato)) {
            agenda.remove(contato);
            System.out.printf("O contato %s foi removido com sucesso.%n", contato.getNome());
        }
    }

    public String buscarContato(Contato contato) {
        for (Contato c : agenda) {
            if (c.equals(contato)) {
                System.out.printf("O contato %s existe na agenda.%n", contato.getNome());
                return c.getNome();
            }
        }
        System.out.printf("O contato %s não existe na agenda.%n", contato.getNome());
        return null;
    }

    public boolean validarNC(Contato contato) { // Valida Null, Contains
        if (contato == null) {
            System.out.printf("O contato não está existe na agenda.%n");
            return false;
        } else if (!agenda.contains(contato)) {
            System.out.printf("O %s não está contido na agenda.%n", contato.getNome());
            return false;
        } else {
            return true;
        }
    }

}
