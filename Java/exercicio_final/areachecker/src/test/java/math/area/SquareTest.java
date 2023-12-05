package math.area;

import static org.junit.Assert.*;

import org.junit.Test;

import math.area.classes.Square;

public class SquareTest {
    @Test
    public void testeCalculoAreaQuadrado() {
        // Arrange
        Square square = new Square();
        square.setSize_side(5);

        // Act
        double actualArea = square.calcularArea();

        // Assert
        assertEquals(25.0, actualArea, 0.0001);
    }
}
