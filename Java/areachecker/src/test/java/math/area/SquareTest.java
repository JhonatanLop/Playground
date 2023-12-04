package math.area;

import static org.junit.Assert.*;

import org.junit.Test;

import math.area.Classes.Square;

public class SquareTest {
    @Test
    public void testeCalculoAreaQuadrado() {
        // Arrange
        Square square = new Square();
        square.setSize_side(5);

        // Act
        square.calculate_area(square);

        // Assert
        assertEquals(25.0, square.getArea(), 0.0001);
    }
}