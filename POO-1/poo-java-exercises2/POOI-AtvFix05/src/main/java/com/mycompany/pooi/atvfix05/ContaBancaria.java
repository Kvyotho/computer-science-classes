
package com.mycompany.pooi.atvfix05;


public class ContaBancaria {
    
    private String titular;
    private double saldo;
    private int numero;
    
    public ContaBancaria(String titular, double saldo, int numero){
        this.titular = titular;
        this.saldo = saldo;
        this.numero = numero;
    }
    
    public void depositar(double valor){
        if(valor > 0){
            saldo += valor;
            System.out.printf("%.2f R$ Transferidos%nNovo Saldo: %.2f%n", valor, saldo);
        }
    }
    public void depositarPara(ContaBancaria conta, double valor){
        if(valor > 0 && saldo >= valor){
            saldo -= valor;
            conta.saldo += valor;
            System.out.printf("%.2f R$ Transferidos para %s%nNovo Saldo: %.2f%n", valor, conta.titular, saldo);
        }else{
            System.out.println("Valor de deposito inválido.");
        }
    }
    
    public void sacar(double valor){
        if(valor <= saldo){
            saldo -= valor;
            System.out.printf("%.2f R$ Sacados%nNovo Saldo: %.2f%n", valor, saldo);
        }else{
            System.out.println("Saldo insuficiente.");
        }
    }
    
    public void exibirSaldo(){
        System.out.printf("Titular: %s%nSaldo: %.2f%nNumero: %d%n%n", titular, saldo, numero);
    }
    
}
