package com.atvavapoo.Q3;

public class Funcionario implements Bonificavel{
    protected String nome;
    protected double salario;

    public Funcionario(String nome, double salario){
        this.nome = nome;
        this.salario = salario;
    }

    @Override
    public double calcularBonus(){
        return (salario * 0.10);
    }
}
