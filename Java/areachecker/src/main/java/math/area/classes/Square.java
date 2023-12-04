package math.area.classes;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Square {
    double size_side;
    double area;

    public void calculate_area(Square square) {
        // formula para quadrado
        // lado * lado
        double area = square.getSize_side() * square.getSize_side();
        square.setArea(area);
    }
}
