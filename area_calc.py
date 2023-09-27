# area_calc.py
from area.rectangle import Rect
from area.square import Square
from area.circle import Circle
from area.Triangle import Tri
from area.Parallelogram import Paral
from area.Ellipse import Ell


if __name__ == '__main__':
    sq1 = Square(5)
    print(sq1)


    rect1 = Rect(5, 10)
    rect2 = Rect(8, 9)
    print(rect1)
    print(rect2)

    cir1 = Circle(2)
    print(cir1)

    tri1 = Tri(2,1)
    print(tri1)

    paral1 = Paral(4,1)
    print(paral1)

    ell1 = Ell(2,4)
    print(ell1)


#%%
