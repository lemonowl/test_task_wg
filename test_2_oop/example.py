from engine.models import Circle, Triangle, Rectangle
from engine import Engine2D


circle = Circle((2, 0), 5.7)
triangle = Triangle((2, 3), (-5, 0), (3, -2))
rectangle = Rectangle((5, 7), (8, 3), 4)
circle2 = Circle((-1, 5), 3)
triangle2 = Triangle((4, -4), (7, 2), (-3, -2))
rectangle2 = Rectangle((-2, 0), (6, -1), 7.8)

# Каждая фигура должна иметь метод draw
circle.draw()
triangle.draw()
rectangle.draw()
print()

engine1 = Engine2D()
engine1.add_figures(circle, rectangle, triangle)
engine1.draw()
print()

# Добавить возможность менять цвет отрисовки
engine1.set_color('red')
engine1.add_figures(circle, rectangle, triangle)
engine1.set_color('white')
engine1.add_figures(circle2, triangle2, rectangle2)
engine1.draw()

