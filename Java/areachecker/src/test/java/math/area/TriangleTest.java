package math.area;

import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;

import math.area.Classes.Triangle;

public class TriangleTest {
    @Test
    public void testCalculateAreaEquilateralTriangle() {
        // Arrange
        Triangle triangulo = new Triangle();
        triangulo.setQtd_pontos(3);
        List<Integer> medida_lados = Arrays.asList(5, 5, 5);
        triangulo.setSize_side(medida_lados);

        // Act
        triangulo.calculate_area(triangulo);

        // Assert
        assertEquals(10.825317547305483, triangulo.getArea(), 0.0001);
    }

    @Test
    public void testCalculateAreaScaleneTriangle() {
        // Arrange
        Triangle triangulo = new Triangle();
        triangulo.setQtd_pontos(3);
        List<Integer> medida_lados = Arrays.asList(3, 4, 5);
        triangulo.setSize_side(medida_lados);

        // Act
        triangulo.calculate_area(triangulo);

        // Assert
        assertEquals(6.0, triangulo.getArea(), 0.0001);
    }
}
