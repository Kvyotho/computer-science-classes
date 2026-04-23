package com.atvavapoo.Q2;

import java.util.ArrayList;

public class Caixa {

    public void processarPagamentos(ArrayList<Pagamento> pagamentos){
        for (Pagamento p : pagamentos)
            p.processar();
    }

}
