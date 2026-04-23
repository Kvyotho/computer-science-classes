package com.mycompany.aula02atvfix;

import java.util.Scanner;
import java.util.Random;

public class Aula02atvfix {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // --- IF ELSE ---
        // Exec 1
        System.out.println("Digite um número inteiro: ");
        int numero = scanner.nextInt();
        if (numero % 2 == 0) {
            System.out.println("O número é par");
        } else {
            System.out.println("O número é ímpar");
        }

        // Exec 2
        System.out.println("Digite a sua idade: ");
        int idade = scanner.nextInt();
        if (idade >= 18) {
            System.out.println("Você é maior de idade.");
        } else {
            System.out.println("Você é menor de idade.");
        }

        // Exec 3
        System.out.println("Digite o valor do salário mensal: ");
        double bonus;
        double salario = scanner.nextDouble();
        if (salario <= 1000) {
            bonus = salario * 0.10;
            System.out.println("O bonus salarial é: " + bonus);
        } else {
            bonus = salario * 0.05;
            System.out.println("O bonus salarial é: " + bonus);
        }

        // --- SWITCH CASE ---
        // Exec 1
        System.out.println("Digite um número de 1 a 7: ");
        int dia = scanner.nextInt();
        switch (dia) {
            case 1:
                System.out.printf("O número %d corresponde ao Domingo%n", +dia);
                break;
            case 2:
                System.out.printf("O número %d corresponde a Segunda-Feira%n", +dia);
                break;
            case 3:
                System.out.printf("O número %d corresponde a Terça-Feira%n", +dia);
                break;
            case 4:
                System.out.printf("O número %d corresponde a Quarta-Feira%n", +dia);
                break;
            case 5:
                System.out.printf("O número %d corresponde a Quinta-Feira%n", +dia);
                break;
            case 6:
                System.out.printf("O número %d corresponde a Sexta-Feira%n", +dia);
                break;
            case 7:
                System.out.printf("O número %d corresponde ao Sábado%n", +dia);
                break;
        }
        // Exec 2
        System.out.println("Digite um número de 1 a 12: ");
        int mes = scanner.nextInt();
        switch (mes) {
            case 1:
                System.out.printf("O número %d corresponde a Janeiro%n", +mes);
                break;
            case 2:
                System.out.printf("O número %d corresponde a Fevereiro%n", +mes);
                break;
            case 3:
                System.out.printf("O número %d corresponde a Março%n", +mes);
                break;
            case 4:
                System.out.printf("O número %d corresponde a Abril%n", +mes);
                break;
            case 5:
                System.out.printf("O número %d corresponde a Maio%n", +mes);
                break;
            case 6:
                System.out.printf("O número %d corresponde a Junho%n", +mes);
                break;
            case 7:
                System.out.printf("O número %d corresponde a Julho%n", +mes);
                break;
            case 8:
                System.out.printf("O número %d corresponde a Agosto%n", +mes);
                break;
            case 9:
                System.out.printf("O número %d corresponde a Setembro%n", +mes);
                break;
            case 10:
                System.out.printf("O número %d corresponde a Outubro%n", +mes);
                break;
            case 11:
                System.out.printf("O número %d corresponde a Novembro%n", +mes);
                break;
            case 12:
                System.out.printf("O número %d corresponde a Dezembro%n", +mes);
                break;
        }
        // Exec 3
        System.out.println("Digite o preço do produto: ");
        double preco = scanner.nextInt();
        System.out.println("Digite um código de desconto(1, 2, 3): ");
        int codigo = scanner.nextInt();
        switch (codigo) {
            case 1: // 10% off
                System.out.println("O preço com desconto aplicado é: " + preco * 0.90);
                break;
            case 2: // 25% off
                System.out.println("O preço com desconto aplicado é: " + preco * 0.75);
                break;
            case 3: // 50% off
                System.out.println("O preço com desconto aplicado é: " + preco * 0.50);
                break;
        }

        // ---WHILE---
        // Exec 1
        System.out.println("Digite um número: ");
        int n0 = 0;
        int n1 = scanner.nextInt();
        if (n1 <= 0) {
            System.out.println("Erro. Digite um número maior que zero");
        } else {
            while (n1 > n0) {
                n0++;
                System.out.println(n0);
            }
        }

        // Exec 2
        int n2 = 0;
        int soma = 0;
        while (n2 >= 0) {
            soma = soma + n2;
            System.out.println("Digite uma sequência de números inteiros:");
            n2 = scanner.nextInt();
        }
        System.out.println("A soma dos números digitados é: " + soma);

        // Exec 3
        Random random = new Random();
        int rng = random.nextInt(101);
        System.out.println("Adivinhe o número aleatório(1 a 100): ");
        int guess = scanner.nextInt();
        while (guess != rng) {
            if (guess > rng) {
                System.out.printf("O número aleatório é menor do que %d.%n", +guess);
                System.out.println("Tente novamente: ");
                guess = scanner.nextInt();
            } else {
                System.out.printf("O número aleatório é maior do que %d.%n", +guess);
                System.out.println("Tente novamente: ");
                guess = scanner.nextInt();
            }
        }

        System.out.println("Você acertou o número.");

        // ---DO WHILE---
        // Exec 1
        int n03 = 0;
        do {
            System.out.println("Digite um número maior que zero: ");
            n03 = scanner.nextInt();
        } while (n03 <= 0);
        do {
            System.out.println(n03);
            n03--;
        } while (n03 != 0);

        // Exec 2
        System.out.println("Digite a sua senha: ");
        String senha = scanner.next();
        String confirmar;
        do {
            System.out.println("Confirme a sua senha: ");
            confirmar = scanner.next();
        } while (!senha.equals(confirmar));
        System.out.println("Senha confirmada.");

        // Exec 3
        Random random2 = new Random();
        int rng2 = random2.nextInt(101);
        System.out.println("Adivinhe o número aleatório(1 a 100): ");
        int guess2 = scanner.nextInt();
        do {
            if (guess > rng2) {
                System.out.printf("O número aleatório é menor do que %d.%n", +guess2);
                System.out.println("Tente novamente: ");
                guess2 = scanner.nextInt();
            } else {
                System.out.printf("O número aleatório é maior do que %d.%n", +guess2);
                System.out.println("Tente novamente: ");
                guess2 = scanner.nextInt();
            }
        } while (guess != rng2);

        // --- FOR ---
        // Exec 1
        System.out.println("Digite um número para tabuada: ");
        int tabuada = scanner.nextInt();
        for (int i = 1; i < 11; i++) {
            System.out.println(tabuada * i);
        }
        // Exec 2
        for (int i = 10; i > -1; i--) {
            System.out.println(i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        // Exec 3
        int somapar = 0;
        System.out.println("Soma dos números pares até 100: ");

        for (int i = 0; i < 100; ++i) {
            if (i % 2 == 0) {
                somapar += i;
            }
        }
        System.out.printf("%d", somapar);

        scanner.close();
    }
}
