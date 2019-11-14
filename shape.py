from typing import List
from zope.interface import implementer, Interface
import math
from tkinter import *
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
        self.shape_list = None

    def create_shape_list(self):
        self.shape_list = ShapeList()
        for line in self.file:
            if len(line.split()) == 2:
                mas = line.split(' ')
                self.shape_list.add_shape(Rectangle(int(mas[0]), int(mas[1])))
            elif len(line.split()) == 3:
                mas = line.split(' ')
                self.shape_list.add_shape(
                    Triangle(int(mas[0]), int(mas[1]), int(mas[2])))

    def get_total_results(self):
        self.create_shape_list()
        result = {
            'total_area': self.shape_list.get_total_area(),
            'total_perimeter': self.shape_list.get_total_perimeter()
        }
        return result

def clicked():
    sh = ShapeList()
    numbers = num.get()
    # повтор презентера
    if len(numbers.split()) == 2:
        mas = numbers.split(' ')
        some_class = Rectangle(int(mas[0]), int(mas[1]))
    elif len(numbers.split()) == 3:
        mas = numbers.split(' ')
        some_class = Triangle(int(mas[0]), int(mas[1]), int(mas[2]))
    sh.add_shape(some_class)
    try:
        lb3.configure(text='площадь: %d, периметр: %d' %(sh.get_total_area(), sh.get_total_perimeter()))
    except ValueError:
        lb3.configure(text='фигуры не существует!')


window = Tk()
window.title("Посчитать площадь и периметр фигур")
lbmain = Label(window, text="Программа считает площади и периметры треугольников и прямоугольников")
lbmain.grid(column=0, row=0)
lbl = Label(window, text="Введите размеры сторон через пробел")
lbl.grid(column=0, row=1)
num = Entry(window, width=20)
num.grid(column=0, row=2)
btn = Button(window, text="Посчитать", command=clicked)
btn.grid(column=0, row=3)
lb2 = Label(window, text="Ответ: ")
lb2.grid(column=0, row=4)
lb3 = Label(window, text="")
lb3.grid(column=0, row=5)
window.mainloop()


# class TestStringMethods(unittest.TestCase):
#     def test_equal(self):
#         self.assertEqual(main_function(), [35, 24, 3, 8, 14.142135623730951, 20])

#
#
# if __name__ == '__main__':
#     unittest.main()
