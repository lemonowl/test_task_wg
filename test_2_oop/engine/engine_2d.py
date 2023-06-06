from .canvas import Canvas


class Engine2D:
    """2D-движок, который умеет “рисовать” простейшие двумерные примитивы на экране
    """
    # холст
    _canvas = Canvas()

    @property
    def canvas(self):
        return self._canvas.items_list

    def add_figures(self, *models):
        """Метод добавления фигур на холст
        """
        self._canvas.add_models(*models)

    def set_color(self, color: str):
        """Сменить цвет отрисовки фигур
        """
        self._canvas.set_color(color)

    def draw(self):
        """Метод отрисовки всех объектов на холсте с очисткой очереди отрисовки
        """
        self._canvas.draw()
        self._canvas.clear_canvas()
