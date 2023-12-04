package math.area;

import org.junit.Test;

import math.area.classes.Diamond;

public class DiamondTest {
    
    @Test
    public void testCalculateArea() {
        Diamond diamond = new Diamond();
        diamond.setLarger_diagonal(10);
        diamond.setSmaller_diagonal(5);
        diamond.calcularArea();
        assert(diamond.getArea() == 25);
    }
}
