package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import math.area.interfaces.Shape;

@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor

public class Circle implements Shape{
    private double radius;
    private double area;

    public double calcularArea() {
        // formula para circulo
        // pi * raio²
        setArea(area);
        return getArea();
    }
}
