
class Figure:
    """Прототип фигур для добавления на холст
    """
    _object_name = None
    color: str = None

    def set_color(self, color):
        self.color = color

    def _get_drawing_text(self, object_params):
        """Вспомогательный метод для вывода текста отрисовки фигуры
        """
        color = f' and color {self.color}' if self.color else ''
        return f'Drawing {self._object_name}: {object_params}{color}'

    def draw(self):
        raise NotImplementedError('Необходимо имлементировать метод для унаследованного класса')
