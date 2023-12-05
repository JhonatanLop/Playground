package math.area.classes;

import math.area.interfaces.Calculable;
import math.area.interfaces.CalculableFactory;

public class CalculableCreator implements CalculableFactory{
    public Calculable createSquare() { return new Square(); }
    public Calculable createRectangle() { return new Rectangle(); }
    public Calculable createCircle() { return new Circle(); }
    public Calculable createTriangle() { return new Triangle(); }
    public Calculable createParallelogram() { return new Parallelogram(); }
    public Calculable createTrapeze() { return new Trapeze(); }
    public Calculable createHexagon() { return new Hexagon(); }
    public Calculable createRhombus() { return new Rhombus(); }
    public Calculable createCube() { return new Cube(); }
}
