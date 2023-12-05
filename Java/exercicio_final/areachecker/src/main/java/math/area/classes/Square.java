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

public class Square implements Calculable{
    double size_side;
    double area;

    public double calcularArea() {
        // formula para quadrado
        // lado * lado
        double area = size_side * size_side;
        setArea(area);
        return getArea();
    }
}
