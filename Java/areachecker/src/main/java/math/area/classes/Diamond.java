package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class Diamond {
    double lerger_diagonal;
    double smaller_diagonal;
    double area;

    public void calculate_area(Diamond diamond) {
        // formula para losango
        // (diagonal maior * diagonal menor) / 2
        double area = (diamond.getLerger_diagonal() * diamond.getSmaller_diagonal()) / 2;
        diamond.setArea(area);
    }
}
