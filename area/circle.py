from area.shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.cir_area = 0.0
        self.radius = radius

    def area(self):
        self.cir_area = self.radius * self.radius * 3.14
        return self.cir_area

    def __str__(self) -> str:
        return 'Circle Area of ' + str(self.radius) + 'U :' + str(self.area())
#%%
