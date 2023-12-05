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

public class Rectangle implements Shape{
    private double base;
    private double height;
    private double area;

    public double calcularArea() {
        // formula para retangulo
        // base * altura
        double area = getBase() * getHeight();
        setArea(area);
        return getArea();
    }
}
