package com.mycompany.pooi.atvfix05;

//import java.util.ArrayList;
//import java.util.Arrays;

public class POOIAtvFix05 {

    public static void main(String[] args) {
        // 1)
        System.out.printf("Exec 1: %n%n");
        Pessoa p1 = new Pessoa("nometeste1", 111, "cidadeteste1");
        Pessoa p2 = new Pessoa("nometeste2", 222, "cidadeteste2");
        Pessoa p3 = new Pessoa("nometeste3", 333, "cidadeteste3");

        p1.exibirInfo();
        p2.exibirInfo();
        p3.exibirInfo();

        // 2)
        System.out.printf("%nExec 2: %n%n");
        ContaBancaria c1 = new ContaBancaria("titular1", 1000, 123456);
        ContaBancaria c2 = new ContaBancaria("titular2", 2000, 222333);

        c1.exibirSaldo();
        c1.depositarPara(c2, 1000);
        c2.exibirSaldo();
        c1.depositarPara(c2, 9999);
        c2.sacar(1250);
        c2.depositarPara(c1, 250);
        c2.exibirSaldo();
        c1.exibirSaldo();

        // 3)
        System.out.printf("%nExec 3: %n%n");
        Produto prod1 = new Produto("p1", 25, 10);
        Produto prod2 = new Produto("p2", 50, 12);
        Produto prod3 = new Produto("p3", 100, 10);

        System.out.printf("Valor total do estoque do produto %s: %.2f%n", prod1.getNome(), prod1.totalProduto());
        System.out.printf("Valor total do estoque do produto %s: %.2f%n", prod2.getNome(), prod2.totalProduto());
        System.out.printf("Valor total do estoque do produto %s: %.2f%n", prod3.getNome(), prod3.totalProduto());

        System.out.printf("Valor total do estoque geral: %.2f%n", Produto.totalEstoque());

        // 4)
        System.out.printf("%nExec 4: %n%n");
        Carro car1 = new Carro("marca1", "modelo1", 2022, 90);
        Carro car2 = new Carro("marca1", "modelo2", 2024, 50);

        car1.acelerar(10);
        car2.acelerar(100);
        Carro.testeCorrida(car1, car2);
        car2.frear(200);
        Carro.testeCorrida(car1, car2);
        car2.acelerar(150);
        Carro.testeCorrida(car1, car2);

        // 5)
        System.out.printf("%nExec 5: %n%n");
        Aluno aluno1 = new Aluno("aluno1", 5, 10, 10);
        Aluno aluno2 = new Aluno("aluno2", 3, 6, 2);
        Aluno aluno3 = new Aluno("aluno3", 10, 9, 7);

        aluno1.calcMedia();
        aluno2.calcMedia();
        aluno3.calcMedia();

        // 6
        System.out.printf("%nExec 6: %n%n");
        Retangulo r1 = new Retangulo(10, 20);
        Retangulo r2 = new Retangulo(5, 25);

        System.out.printf("A área do retangulo r1 é %d%n", r1.calcArea());
        System.out.printf("A área do retangulo r2 é %d%n", r2.calcArea());
        System.out.printf("O perimetro do retangulo r1 é: %d%n", r1.calcPerimetro());
        System.out.printf("O perimetro do retangulo r2 é: %d%n", r2.calcPerimetro());

        r1.compararRetangulo(r2);

        // 7
        System.out.printf("%nExec 7: %n%n");
        Livro l1 = new Livro("Livro1", "autor1");
        Livro l2 = new Livro("Livro2", "autor1");
        Livro l3 = new Livro("Livro3", "autor2");
        Livro l4 = new Livro("Livro4", "autor3");

        Biblioteca b1 = new Biblioteca();
        b1.addLivro(l1);
        b1.devolverLivro(l1);
        b1.devolverLivro(l2);
        b1.emprestarLivro(l1);
        b1.devolverLivro(l1);
        b1.addLivro(l2);
        b1.addLivro(l3);
        b1.removerLivro(l4);
        b1.removerLivro(l3);

        // 8)
        System.out.printf("%nExec 8: %n%n");

        System.out.println(Calculadora.somar(2, 4));
        System.out.println(Calculadora.subtrair(20, 10));
        System.out.println(Calculadora.multipicar(5, 5));
        System.out.println(Calculadora.dividir(1024, 2));

        // 9
        System.out.printf("%nExec 9: %n%n");
        Contato cont1 = new Contato("contato1", "123-456");
        Contato cont2 = new Contato("contato2", "111-344");
        Contato cont3 = new Contato("contato3", "132-555");

        Agenda agenda1 = new Agenda();

        agenda1.addContato(cont1);
        agenda1.addContato(cont2);
        agenda1.addContato(cont3);
        agenda1.removeContato(cont3);
        agenda1.buscarContato(cont1);
        agenda1.buscarContato(cont3);

        // 10
        System.out.printf("%nExec 10: %n%n");

        Personagem per1 = new Personagem("personagem1", 10, 5);
        Personagem per2 = new Personagem("personagem2", 10, 2);

        per2.exibirVida();
        per1.atacar(per2);
        per2.exibirVida();
        per2.atacar(per1);
        per1.exibirVida();

        per1.atacar(per2);
        per2.exibirVida();
    }

}
