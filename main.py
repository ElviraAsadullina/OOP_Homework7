from Shapes import Circle, Square, Triangle


def main():
    circle = Circle(5)
    square = Square(5)
    triangle = Triangle(5, 7, 57)

    for el in (circle, square, triangle):
        print(f'{el.__class__.__name__}: площадь равна: {el.get_square()}')
        print(el.name)

    print(circle.radius)
    try:
        circle.radius = -7
    except ValueError as e:
        print(e)

    square.side = -11
    print(square.side)


if __name__ == '__main__':
    main()