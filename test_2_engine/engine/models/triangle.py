from ..prototypes import Figure


class Triangle(Figure):
    """Примитив Треугольник
    """
    _object_name = 'Triangle'
    # координата вершины A прямоугольника
    _apex_a: tuple
    # координата вершины B прямоугольника
    _apex_b: tuple
    # координата вершины C прямоугольника
    _apex_c: tuple

    def __init__(self, apex_a: tuple, apex_b: tuple, apex_c: tuple):
        self._apex_a = apex_a
        self._apex_b = apex_b
        self._apex_c = apex_c

    @property
    def apex_a(self):
        return self._apex_a

    @property
    def apex_b(self):
        return self._apex_b

    @property
    def apex_c(self):
        return self._apex_c

    def draw(self):
        """Метод отрисовки треугольника
        """
        params = f'A{self.apex_a}, B{self.apex_b}, C{self.apex_c}'
        print(self._get_drawing_text(params))
