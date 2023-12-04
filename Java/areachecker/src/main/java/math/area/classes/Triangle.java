package math.area.classes;

import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Triangle implements Geometry{
    int qtd_pontos;
    List<Integer> size_side;
    double area;

    public double calcularArea() {
        // no caso do triângulo, as medidas do lado listados da seguinte forma:
        // "/" = lista[0]
        // "\" = lista[1]
        // "_" = lista[2]

        // formula para todos os tipos de triângulo
        // semi-perimetro = (a + b + c) / 2
        // area = raiz do semi-perimetro * (seme-perimetro - a) (semi-perimetro - B) * (semi-perimetro - C)

        double semi_perimetro = (size_side.get(0) + size_side.get(1) + size_side.get(2)) / 2;
        double area = Math.sqrt(semi_perimetro * (semi_perimetro - size_side.get(0))
                * (semi_perimetro - size_side.get(1)) * (semi_perimetro - size_side.get(2)));
        setArea(area);
        return getArea();
    }
}
