package com.atvavapoo.Q5;

import java.io.*;
import java.util.ArrayList;

public class RelatorioVendas {

    private final String arquivo = "vendas.txt";

    public void registrarVenda(String produto, double valor) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(arquivo, true))) {
            bw.write(produto + ";" + valor);
            bw.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void listarVendas() {
        try (BufferedReader br = new BufferedReader(new FileReader(arquivo))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                System.out.println(linha);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public double calcularTotalVendido() {
        double total = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(arquivo))) {
            String linha;

            while ((linha = br.readLine()) != null) {
                String[] partes = linha.split(";");
                double valor = Double.parseDouble(partes[1]);
                total += valor;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        return total;
    }
}
