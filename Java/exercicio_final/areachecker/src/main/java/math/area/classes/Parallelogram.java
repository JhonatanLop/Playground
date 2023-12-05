package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import math.area.interfaces.Calculable;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class Parallelogram implements Calculable{
    private double height;
    private double base;
    private double area;

    public double calcularArea() {
        // formula para paralelogramo
        // base * altura
        double area = base * height;
        setArea(area);
        return getArea();
    }
}
