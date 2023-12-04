package math.area;

import static org.junit.Assert.*;

import org.junit.Test;

import math.area.classes.Circle;

public class CircleTest {
    
    @Test
    public void testCalculoAreaCirculoWithZeroRadius() {
        // Arrange
        Circle circle = new Circle();
        circle.setRadius(0);
    
        // Act
        circle.calcularArea();
    
        // Assert
        assertEquals(0, circle.getArea(), 0.0001);
    }
    
    @Test
    public void testCalculoAreaCirculoWithNegativeRadius() {
        // Arrange
        Circle circle = new Circle();
        circle.setRadius(-5);
    
        // Act
        circle.calcularArea();
    
        // Assert
        assertEquals(0, circle.getArea(), 0.0001);
    }
}