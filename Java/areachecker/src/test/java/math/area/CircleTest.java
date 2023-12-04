package math.area;

import static org.junit.Assert.*;

import org.junit.Test;

import math.area.Classes.Circle;

public class CircleTest {
    @Test
    public void testeCalculoAreaCirculo() {
        // Arrange
        Circle circle = new Circle();
        circle.setRadius(5);

        // Act
        circle.calculate_area(circle);

        // Assert
        assertEquals(78.53981633974483, circle.getArea(), 0.0001);
    }
}
