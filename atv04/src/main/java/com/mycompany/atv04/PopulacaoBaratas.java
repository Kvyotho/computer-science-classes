package com.mycompany.atv04;

import java.util.Random;

public class PopulacaoBaratas {

    Random rand = new Random();
    int pop = rand.nextInt(1000);
    
    public void aumentaBaratas(){
    pop += (pop * 0.10);
}
    public void spray(){
    pop -= (pop * 0.10); 
    }
    public double getNumeroBaratas(){
        System.out.println(pop);
        return pop;
    }
}
