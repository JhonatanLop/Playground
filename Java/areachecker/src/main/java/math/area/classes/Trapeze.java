package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class Trapeze implements Geometry{
    private double height;
    private double smaller_base;
    private double larger_base;
    private double area;

    public double calcularArea() {
        // formula para trapezio
        // (base maior + base menor) * altura / 2
        double area = ((larger_base + smaller_base) * height) / 2;
        setArea(area);
        return getArea();
    }
}