package math.area.classes;

public class Hexagon {
    private double sideLength;

    public Hexagon(double sideLength) {
        this.sideLength = sideLength;
    }

    public double calcularArea() {
        double apothem = sideLength * Math.sqrt(3) / 2;
        return (3 * Math.sqrt(3) * sideLength * sideLength) / 2;
    }
}
