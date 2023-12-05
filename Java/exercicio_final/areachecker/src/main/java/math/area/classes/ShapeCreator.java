package math.area.classes;

import math.area.interfaces.Shape;
import math.area.interfaces.ShapeFactory;

public class ShapeCreator implements ShapeFactory{
    public Shape createSquare() { return new Square(); }
    public Shape createRectangle() { return new Rectangle(); }
    public Shape createCircle() { return new Circle(); }
    public Shape createTriangle() { return new Triangle(); }
    public Shape createParallelogram() { return new Parallelogram(); }
    public Shape createTrapeze() { return new Trapeze(); }
    public Shape createHexagon() { return new Hexagon(); }
    public Shape createRhombus() { return new Rhombus(); }
    public Shape createCube() { return new Cube(); }
}
