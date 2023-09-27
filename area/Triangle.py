from area.shape import Shape


class Tri(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tri_area = 0.0

    def __str__(self):
        return ('Triangle Area of '
                + str(self.width) + 'Ux' + str(self.height)
                + 'U :' + str(self.area()))
    def area(self):
        self.tri_area = self.width * self.height * 0.5
        return self.tri_area


#%%
