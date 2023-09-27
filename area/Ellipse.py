from area.shape import Shape


class Ell(Shape):
    def __init__(self, ra1, ra2):
        self.ell_area = 0.0
        self.radius1 = ra1
        self.radius2 = ra2

    def area(self):
        self.ell_area = self.radius1 * self.radius2 * 3.14
        return self.ell_area

    def __str__(self) -> str:
        return 'Ellipse Area of ' + str(self.radius1) + 'Ux' + str(self.radius2) + 'U :' + str(self.area())
#%%
