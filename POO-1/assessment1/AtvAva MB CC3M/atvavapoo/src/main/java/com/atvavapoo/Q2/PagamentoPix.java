package com.atvavapoo.Q2;

public class PagamentoPix extends Pagamento{
    private String numeroPix;

    public PagamentoPix(double valor, String numeroPix){
        super(valor);
        this.numeroPix = numeroPix;
    }

    @Override
    public void processar(){
        System.out.println("Pagamento no Pix em R$ "+valor+" foi processado");
    }
    
}