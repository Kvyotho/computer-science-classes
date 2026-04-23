package com.atvavapoo.Q2;

public class PagamentoCartao extends Pagamento{
    private String numeroCartao;

    public PagamentoCartao(double valor, String numeroCartao){
        super(valor);
        this.numeroCartao = numeroCartao;
    }

    @Override
    public void processar(){
        System.out.println("Pagamento no Cartão em R$ "+valor+" foi processado");
    }
    
}
