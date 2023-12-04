package math.area;

import org.junit.Test;

import math.area.Classes.Diamond;

public class DiamondTest {
    
    @Test
    public void testCalculateArea() {
        Diamond diamond = new Diamond();
        diamond.setLerger_diagonal(10);
        diamond.setSmaller_diagonal(5);
        diamond.calculate_area(diamond);
        assert(diamond.getArea() == 25);
    }
}
