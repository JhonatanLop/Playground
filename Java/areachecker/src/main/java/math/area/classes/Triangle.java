package math.area.classes;

import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import math.area.interfaces.Shape;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class Triangle implements Shape{
    int qtd_pontos;
    List<Integer> sizeSide;
    double area;
    String type;

    public double calcularArea() {
        // no caso do triângulo, as medidas do lado listados da seguinte forma:
        // "/" = lista[0]
        // "\" = lista[1]
        // "_" = lista[2]

        // formula para o triângulo escaleno
        if (sizeSide.get(0) != sizeSide.get(1) && sizeSide.get(0) != sizeSide.get(2)
                && sizeSide.get(1) != sizeSide.get(2)) {
            // semi-perimetro = (a + b + c) / 2
            // area = raiz do semi-perimetro * (seme-perimetro - a) (semi-perimetro - B) * (semi-perimetro - C)
    
            double semi_perimetro = (sizeSide.get(0) + sizeSide.get(1) + sizeSide.get(2)) / 2;
            double area = Math.sqrt(semi_perimetro * (semi_perimetro - sizeSide.get(0))
                    * (semi_perimetro - sizeSide.get(1)) * (semi_perimetro - sizeSide.get(2)));
            setArea(area);
            return getArea();
        } else
        // formula para o triângulo equilatero
        if (sizeSide.get(0) == sizeSide.get(1) && sizeSide.get(0) == sizeSide.get(2)
                && sizeSide.get(1) == sizeSide.get(2)) {
            // area = (lado * lado * raiz de 3) / 4
            double area = (sizeSide.get(0) * sizeSide.get(0) * Math.sqrt(3)) / 4;
            setArea(area);
            return getArea();
        } else
        // formula para o triângulo isósceles
        if (sizeSide.get(0) == sizeSide.get(1) && sizeSide.get(0) != sizeSide.get(2)
                || sizeSide.get(0) == sizeSide.get(2) && sizeSide.get(0) != sizeSide.get(1)
                || sizeSide.get(1) == sizeSide.get(2) && sizeSide.get(1) != sizeSide.get(0)) {
            // area = (base * altura) / 2
            // altura = raiz de (lado * lado) - (base * base) / 4
            // base = lado diferente
            int base = 0;
            int altura = 0;
            if (sizeSide.get(0) == sizeSide.get(1)) {
                base = sizeSide.get(2);
                altura = (int) Math.sqrt((sizeSide.get(0) * sizeSide.get(0)) - (base * base) / 4);
            } else if (sizeSide.get(0) == sizeSide.get(2)) {
                base = sizeSide.get(1);
                altura = (int) Math.sqrt((sizeSide.get(0) * sizeSide.get(0)) - (base * base) / 4);
            } else if (sizeSide.get(1) == sizeSide.get(2)) {
                base = sizeSide.get(0);
                altura = (int) Math.sqrt((sizeSide.get(1) * sizeSide.get(1)) - (base * base) / 4);
            }
            double area = (base * altura) / 2;
            setArea(area);
            return getArea();
        }
        // formula para o triângulo retângulo
        else {
            // area = (cateto * cateto) / 2
            // cateto = lado diferente
            // item 0 é a altura e 2 é a base
            double area = (sizeSide.get(0) * sizeSide.get(2)) / 2;
            setArea(area);
            return getArea();
        }
    }
}
