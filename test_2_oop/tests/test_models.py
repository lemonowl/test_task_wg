import pytest
from test_2_oop.engine.models import Circle, Triangle, Rectangle


class TestModels:
    """Тесты примитивов Circle, Triangle, Rectangle
    """
    drawing_text = 'Drawing {}: {}'
    color = ' and color {}'

    object_name = 'Circle'
    center = (0, 1)
    radius = 5
    params = f'O{center} with radius {radius}'

    @staticmethod
    def get_captured_out(capsys):
        captured = capsys.readouterr()
        return captured.out.replace('\n', '')

    def test_01_draw_circle(self, capsys):
        """Тест метода отрисовки окружности
        """
        standard = self.drawing_text.format(self.object_name, self.params)

        circle = Circle(self.center, self.radius)
        circle.draw()
        assert self.get_captured_out(capsys) == standard

    def test_02_set_color(self, capsys):
        """Тест метода отрисовки окружности
        """
        color = 'white'
        standard = f'{self.drawing_text.format(self.object_name, self.params)}{self.color.format(color)}'

        circle = Circle(self.center, self.radius)
        circle.set_color(color)
        circle.draw()
        assert self.get_captured_out(capsys) == standard

    def test_03_triangle(self, capsys):
        """Тест метода отрисовки треугольника
        """
        object_name = 'Triangle'
        apex_a = (0, 1)
        apex_b = (-1, 3)
        apex_c = (2, -2)
        params = f'A{apex_a}, B{apex_b}, C{apex_c}'
        standard = self.drawing_text.format(object_name, params)

        triangle = Triangle(apex_a, apex_b, apex_c)
        triangle.draw()
        assert self.get_captured_out(capsys) == standard

    def test_04_rectangle(self, capsys):
        """Тест метода отрисовки прямоугольника
        """
        object_name = 'Rectangle'
        apex_a = (0, 0)
        apex_b = (-2, -4)
        length = 3.5
        params = f'A{apex_a}, B{apex_b} with second side length {length}'
        standard = self.drawing_text.format(object_name, params)

        rectangle = Rectangle(apex_a, apex_b, length)
        rectangle.draw()
        assert self.get_captured_out(capsys) == standard
