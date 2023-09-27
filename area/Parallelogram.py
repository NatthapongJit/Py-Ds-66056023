from area.shape import Shape


class Paral(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paral_area = 0.0

    def __str__(self) :
        return ('Parallelogram Area of '
                + str(self.width) + 'Ux' + str(self.height)
                + 'U :' + str(self.area()))

    def area(self):
        self.paral_area = self.width * self.height
        return self.paral_area
#%%
