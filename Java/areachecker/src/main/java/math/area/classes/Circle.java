package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor

public class Circle {
    double radius;
    double area;

    public void calculate_area(Circle circle) {
        // formula para circulo
        // pi * raio²
        double area = Math.PI * circle.getRadius() * circle.getRadius();
        circle.setArea(area);
    }
}
