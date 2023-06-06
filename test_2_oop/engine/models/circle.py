from ..prototypes import Figure


class Circle(Figure):
    """Примитив Окружность
    """
    _object_name = 'Circle'
    _center: tuple
    _radius: [int, float]

    def __init__(self, center: tuple, radius: [int, float]):
        """
        :param center: координата центра окружности
        :param radius: радиус окружности
        """
        self._center = center
        self._radius = radius

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    def draw(self):
        """Метод отрисовки окружности
        """
        params = f'O{self.center} with radius {self.radius}'
        print(self._get_drawing_text(params))
