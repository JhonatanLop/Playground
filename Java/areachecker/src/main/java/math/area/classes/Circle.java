package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor

public class Circle implements Geometry{
    private double radius;
    private double area;

    public double calcularArea() {
        // formula para circulo
        // pi * raio²
        setArea(area);
        return getArea();
    }
}
