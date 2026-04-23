package com.atvavapoo.Q3;

import java.util.ArrayList;

public class FinanceiroBonus {

    public double totalGastoBonus(ArrayList<Bonificavel> bonificados) {
        double total = 0;
        for (Bonificavel b : bonificados) {
            total += b.calcularBonus();
        }
        return total;
    }
}