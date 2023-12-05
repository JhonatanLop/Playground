package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class Cube implements Shape {
    private double side;
    private double area;

    public double calcularArea() {
        // formula para cubo
        // lado³
        double area = side * side * side;
        setArea(area);
        return getArea();
    }
}
