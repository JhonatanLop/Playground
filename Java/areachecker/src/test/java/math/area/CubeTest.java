package math.area;

import org.junit.Test;

import math.area.classes.Cube;

public class CubeTest {
    
    @Test
    public void testCalculateArea() {
        Cube cube = new Cube();
        cube.setSide(5);
        cube.calculate_area(cube);
        assert(cube.getArea() == 125);
    }
}
