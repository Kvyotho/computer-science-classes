package com.mycompany.atv04;

public class Cozinha {
    PopulacaoBaratas pbc = new PopulacaoBaratas();

    public void simular() {
        pbc.getNumeroBaratas();
        pbc.aumentaBaratas();
        pbc.getNumeroBaratas();
        pbc.spray();
        pbc.getNumeroBaratas();
    }

}