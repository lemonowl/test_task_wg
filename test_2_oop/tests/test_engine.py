from test_2_oop.engine.models import Circle
from test_2_oop.engine import Engine2D


class TestEngine:
    """Тесты движка Engine2D
    """

    def test_01_draw(self, capsys):
        """Проверяет отрисовку объектов и очистку холста
        """
        center = (1, 2)
        radius = 3
        circle = Circle(center, radius)

        engine = Engine2D()
        engine.add_figures(circle)
        engine.draw()
        captured = capsys.readouterr()
        assert captured.out != '' and engine._canvas.items_list == []
