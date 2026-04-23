package com.atvavapoo.Q4;

import java.util.ArrayList;

public class Pedido {
    private String data;
    private double valorTotal;
    private String status;
    private ArrayList<ItemPedido> itens = new ArrayList<>();

    public Pedido(String data){
        this.data = data;
        this.status = "Em preparo";
    }

    public void adicionarItemPedido(ItemPedido item) {
        if (item != null) {
            itens.add(item);
            calcularTotal();
        }
    }

    public void calcularTotal() {
        valorTotal = 0;
        for (ItemPedido i : itens) {
            valorTotal += i.getSubtotal();
        }

    }

    public void alterarStatus(String novoStatus) throws StatusInvalidoException{
        if(status.equals("Em Preparo") && novoStatus.equals("Saiu para Entrega")){
            status = novoStatus;
        }
        else if(status.equals("Saiu para Entrega") && novoStatus.equals("Entregue")){
            status = novoStatus;
        } else {
            throw new StatusInvalidoException("Mudança de Status inválida");
        }
    }
}
