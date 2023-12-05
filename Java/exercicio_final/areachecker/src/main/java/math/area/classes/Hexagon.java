package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import math.area.interfaces.Shape;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class Hexagon implements Shape{
    private double sideLength;
    private double area;

    public double calcularArea() {
        // formula para o hexágono
        // (3 * raiz(3) * lado²) / 2
        double area = (6 * Math.pow(sideLength, 2) * Math.sqrt(3)) / 4;
        setArea(area);
        return getArea();
    }
}
