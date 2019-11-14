from typing import List
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
    def __init__(self):
        self.shapes: List[IShape] = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def get_total_area(self):
        total_area = 0
        for shape in self.shapes:
            total_area += shape.get_area()
        return total_area

    def get_total_perimeter(self):
        total_perimeter = 0
        for shape in self.shapes:
            total_perimeter += shape.get_perimeter()
        return total_perimeter


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


class Presenter:
    """
    Класс обработки полученного файла
    """
    def __init__(self, file):
        self.file: str = file

    def create_shape_list(self):
        shape_list = ShapeList()
        for line in self.file:
            if len(line.split()) == 2:
                mas = line.split(' ')
                shape_list.add_shape(Rectangle(int(mas[0]), int(mas[1])))
            elif len(line.split()) == 3:
                mas = line.split(' ')
                shape_list.add_shape(
                    Triangle(int(mas[0]), int(mas[1]), int(mas[2])))

        shape_list.get_total_perimeter()
        shape_list.get_total_area()

        return shape_list


# fixme простой пример использования
sh = ShapeList()
rect1 = Rectangle(2, 3)
rect2 = Rectangle(2, 3)
sh.add_shape(rect1)
sh.add_shape(rect2)
print(sh.get_total_perimeter())


# class TestStringMethods(unittest.TestCase):
#     def test_equal(self):
#         self.assertEqual(main_function(), [35, 24, 3, 8, 14.142135623730951, 20])

# def main_function():
#     f = open('text.txt')
#     all = ShapeList(f)
#     return all.create_class()
#
#
# if __name__ == '__main__':
#     unittest.main()
