package math.area;

import static org.junit.Assert.*;

import org.junit.Test;

import math.area.classes.Parallelogram;

public class ParallelogramTest {
    
    @Test
    public void testeCalculoAreaParalelogramo() {
        // Arrange
        Parallelogram parallelogram = new Parallelogram();
        parallelogram.setBase(5);
        parallelogram.setHeight(10);

        // Act
        parallelogram.calculate_area(parallelogram);

        // Assert
        assertEquals(50, parallelogram.getArea(), 0.0001);
    }
}
