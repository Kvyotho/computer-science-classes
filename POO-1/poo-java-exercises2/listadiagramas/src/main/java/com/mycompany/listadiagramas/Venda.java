package com.mycompany.listadiagramas;

import java.time.LocalDateTime;
import java.util.Calendar;

public class Venda {

    int codigo;
    int cliente_codigo;
    LocalDateTime data_venda;

    public void Venda(int codigo, int cliente_codigo, LocalDateTime data_venda) {
        this.codigo = codigo;
        this.cliente_codigo = cliente_codigo;
        this.data_venda = data_venda;
    }

    public void cadastrarVenda(Venda venda) {

    }

    public void consultaVendaPeriodo(LocalDateTime inicio) {
        //Create list of vendas
        //change void return to a list of vendas
        //return the sales between specified start to end
        //inicio = LocalDateTime.now();    
    }

    public void consultaVendaCliente(Cliente cliente) {
        //change void return to list of Venda
    }

}
