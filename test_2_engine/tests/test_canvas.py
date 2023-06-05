import pytest
from test_2_engine.engine.models import Circle
from test_2_engine.engine.canvas import Canvas


class TestCanvas:
    """Тесты холста Canvas
    """
    color = 'white'

    center = (0, 0)
    radius = 1
    circle = Circle(center, radius)

    def test_01_set_color(self):
        """Проверка метода set_color
        """
        canvas = Canvas()
        canvas.set_color(self.color)
        assert canvas.color == self.color

    def test_02_add_model(self):
        """Проверка добавления объектов на холст
        """
        standard = [self.circle]

        canvas = Canvas()
        canvas.set_color(self.color)
        canvas.add_models(self.circle)
        assert canvas.items_list == standard and self.circle.color == self.color

    def test_03_add_model_negative(self):
        """Проверка добавления объектов на холст с измененным цветом
        """
        canvas = Canvas()
        with pytest.raises(TypeError):
            canvas.add_models(canvas)

    def test_04_draw(self, capsys):
        """Проверка метода отрисовки объектов холста
        """
        canvas = Canvas()
        canvas.add_models(self.circle)
        canvas.draw()
        captured = capsys.readouterr()
        assert captured.out != ''

    def test_05_clear_canvas(self):
        """Проверка очистки холста
        """
        canvas = Canvas()
        canvas.add_models(self.circle)
        canvas.clear_canvas()
        assert canvas.items_list == []
