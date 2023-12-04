package math.area.Classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class Trapeze {
    double height;
    double smaller_base;
    double larger_base;
    double area;

    public void calculate_area(Trapeze trapeze) {
        // formula para trapezio
        // (base maior + base menor) * altura / 2
        double area = ((trapeze.getLarger_base() + trapeze.getSmaller_base()) * trapeze.getHeight()) / 2;
        trapeze.setArea(area);
    }
}
