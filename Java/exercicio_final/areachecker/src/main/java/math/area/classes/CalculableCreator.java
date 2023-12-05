package math.area.classes;

import java.util.List;

import math.area.interfaces.Calculable;
import math.area.interfaces.CalculableFactory;

public class CalculableCreator implements CalculableFactory{
    public Calculable createSquare(double side) { return new Square(side); }
    public Calculable createRectangle(double base, double height) { return new Rectangle(base, height); }
    public Calculable createCircle(double radius) { return new Circle(radius); }
    public Calculable createTriangle(List<Double> sides) { return new Triangle(sides); }
    public Calculable createParallelogram() { return new Parallelogram(); }
    public Calculable createTrapeze() { return new Trapeze(); }
    public Calculable createHexagon() { return new Hexagon(); }
    public Calculable createRhombus() { return new Rhombus(); }
    public Calculable createCube() { return new Cube(); }
}
