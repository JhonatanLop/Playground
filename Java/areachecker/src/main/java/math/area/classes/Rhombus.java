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

public class Rhombus implements Shape{
    private double larger_diagonal;
    private double smaller_diagonal;
    private double area;

    public double calcularArea() {
        // formula para losango
        // (diagonal maior * diagonal menor) / 2
        double area = (larger_diagonal * smaller_diagonal) / 2;
        setArea(area);
        return getArea();
    }
}