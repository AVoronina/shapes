from zope.interface import implementer, Interface
import math
import unittest


class IShape(Interface):
    """
    Интерфейс для вычисления параметров фигур
    """
    def get_area():
        """
        Вычисление площади фигуры
        """

    def get_perimeter():
        """
        Вычисление периметра фигуры
        """


class ShapeList:
    """
    Класс списка фигур, пришедших на вход
    """
    def __init__(self, f):
        self.f: str = f

    def create_class(self):
        result = []
        for line in self.f:
            if(len(line.split()) == 2):
                mas = line.split(' ')
                rc = Rectangle(int(mas[0]), int(mas[1]))
                result.append(rc.get_area())
                result.append(rc.get_perimeter())
            elif(len(line.split()) == 3):
                mas = line.split(' ')
                tr = Triangle(int(mas[0]), int(mas[1]), int(mas[2]))
                result.append(tr.get_area())
                result.append(tr.get_perimeter())

        return result


@implementer(IShape)
class Rectangle:
    """
    Класс прямоугольника
    """
    def __init__(self, a, b):
        self.a: float = a
        self.b: float = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * (self.a + self.b)


@implementer(IShape)
class Triangle:
    """
    Класс треугольника
    """
    def __init__(self, a, b, c):
        self.a: float = a
        self.b: float = b
        self.c: float = c

    def get_area(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c


class TestStringMethods(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(main_function(), [35, 24, 3, 8, 14.142135623730951, 20])


def main_function():
    f = open('text.txt')
    all = ShapeList(f)
    return all.create_class()


if __name__ == '__main__':
    unittest.main()
