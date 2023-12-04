package math.area.Classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class Parallelogram {
    double height;
    double base;
    double area;

    public void calculate_area(Parallelogram parallelogram) {
        // formula para paralelogramo
        // base * altura
        double area = parallelogram.getBase() * parallelogram.getHeight();
        parallelogram.setArea(area);
    }
}
