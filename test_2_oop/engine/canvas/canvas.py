from ..prototypes.figure import Figure


class Canvas:

    # цвет объектов на холсте
    color: str = None
    # очередь отрисовки
    items_list: list

    def __init__(self):
        self.items_list = []

    def _add_models_in_items_list(self, models):
        for model in models:
            model.set_color(self.color)
            self.items_list.append(model)

    def add_models(self, *models: Figure):
        """Метод добавления фигур на холст
        """
        if not all([isinstance(model, Figure) for model in models]):
            raise TypeError('На холст можно добавлять только примитивы, унаследованные от класса Figure')
        self._add_models_in_items_list(models)

    def set_color(self, color: str):
        """Сменить цвет отрисовки фигур
        """
        self.color = color

    def draw(self):
        """Метод отрисовки объектов на холсте
        """
        for model in self.items_list:
            model.draw()

    def clear_canvas(self):
        """Метод очищает холст
        """
        self.items_list = []
