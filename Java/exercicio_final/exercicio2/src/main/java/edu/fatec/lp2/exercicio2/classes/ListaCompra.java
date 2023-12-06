package edu.fatec.lp2.exercicio2.classes;

import java.util.ArrayList;

import edu.fatec.lp2.exercicio2.interfaces.Calculavel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor

public class ListaCompra implements Calculavel{
    private ArrayList<ItemCompra> itensCompra;
    private int qtdeMax;


    public ListaCompra(int qtdeMax) {
        this.qtdeMax = qtdeMax;
    }

    public void incluir(ItemCompra item) {
        if (this.itensCompra.size() > qtdeMax) {
            System.out.println("Lista cheia");
        } else {
            this.itensCompra.add(item);
        }
    }

    public double CalcularPreco() {
        double precoTotal = 0.0;
        for (ItemCompra item : this.itensCompra) {
            precoTotal += item.CalcularPreco();
        }
        return precoTotal;
    }
}
