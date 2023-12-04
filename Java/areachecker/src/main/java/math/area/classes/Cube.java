package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class Cube {
    double side;
    double area;

    public void calculate_area(Cube cube) {
        // formula para cubo
        // lado³
        double area = cube.getSide() * cube.getSide() * cube.getSide();
        cube.setArea(area);
    }
}
