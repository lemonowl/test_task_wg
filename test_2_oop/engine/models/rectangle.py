from math import sqrt
from ..prototypes import Figure


class Rectangle(Figure):
    """Примитив Прямоугольник
    """
    _object_name = 'Rectangle'
    # координата вершины A прямоугольника
    _apex_a: tuple
    # координата вершины B прямоугольника
    _apex_b: tuple
    # длина второй стороны
    _length: [int, float]

    def __init__(self, apex_a: tuple, apex_b: tuple, length: [int, float]):
        """
        :param apex_a: координата вершины A прямоугольника
        :param apex_b: координата вершины B прямоугольника
        :param length: длина второй стороны
        """
        self._apex_a = apex_a
        self._apex_b = apex_b
        self._length = length

    @property
    def apex_a(self):
        return self._apex_a

    @property
    def apex_b(self):
        return self._apex_b

    @property
    def length(self):
        return self._length

    def draw(self):
        """Метод отрисовки прямоугольника
        """
        params = f'A{self.apex_a}, B{self.apex_b} with second side length {self.length}'
        print(self._get_drawing_text(params))
