from Square import Square
from Circle import Circle

class TestCircle:
    def setup(self):
        self.A = Circle("red", 3)
        self.B = Circle("blue", 5)
        
    def testgetRadius(self):
        assert self.A.getRadius() == 3
        assert self.B.getRadius() == 5
        
    def testsetRadius(self):
        self.A.setRadius(1000)
        assert self.A.radius == 1000
        self.B.setRadius(100)
        assert self.B.radius == 100
        
    def testcomputeself(self):
        assert self.A.computeArea() == (3.14159 * (3**2))
        assert self.B.computeArea() == (3.14159 * (5 ** 2))
        
    def testcomputePerimeter(self):
        assert self.A.computePerimeter() == (3.14159 * 3 * 2)
        assert self.B.computePerimeter() == (3.14159 * 5 * 2)
        
    def testgetShapeProperties(self):
        assert self.A.getShapeProperties() == f"Shape: CIRCLE, Color: {self.A.color}, Radius: {self.A.radius}, " \
               f"Area: {self.A.computeArea()}, Perimiter: {self.A.computePerimeter()}"
        
        assert self.B.getShapeProperties() == f"Shape: CIRCLE, Color: {self.B.color}, Radius: {self.B.radius}, " \
               f"Area: {self.B.computeArea()}, Perimiter: {self.B.computePerimeter()}"

    def testsetColor(self):
        self.A.setColor("magenta")
        assert self.A.color == "magenta"

    def testgetColor(self):
        assert self.A.getColor() == "red"

class TestSquare:
    def setup(self):
        self.A = Square("red", 3)
        self.B = Square("blue", 5)

    def testgetSide(self):
        assert self.A.getSide() == 3
        assert self.B.getSide() == 5

    def testsetSide(self):
        self.A.setSide(1000)
        assert self.A.side == 1000
        self.B.setSide(100)
        assert self.B.side == 100

    def testcomputeself(self):
        assert self.A.computeArea() == (3 ** 2)
        assert self.B.computeArea() == (5 ** 2)

    def testcomputePerimeter(self):
        assert self.A.computePerimeter() == (3 * 4)
        assert self.B.computePerimeter() == (5 * 4)

    def testgetShapeProperties(self):
        assert self.A.getShapeProperties() == f"Shape: SQUARE, Color: {self.A.color}, Side: {self.A.side}, " \
                                              f"Area: {self.A.computeArea()}, Perimiter: {self.A.computePerimeter()}"

        assert self.B.getShapeProperties() == f"Shape: SQUARE, Color: {self.B.color}, Side: {self.B.side}, " \
                                              f"Area: {self.B.computeArea()}, Perimiter: {self.B.computePerimeter()}"

    def testsetColor(self):
        self.A.setColor("magenta")
        assert self.A.color == "magenta"

    def testgetColor(self):
        assert self.A.getColor() == "red"

class testShape2D:
    def setup(self):
        self.A = Shape2D("orange")

    def testsetColor(self):
        self.A.setColor("magenta")
        assert self.A.color == "magenta"

    def testgetColor(self):
        assert self.A.getColor() == "orange"

    def testgetShapeProperties(self):
        assert self.A.getShapeProperties() == f"Shape: N/A, Color: {self.A.color}"
