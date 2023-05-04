# 1.1

# До
# def distance(x1, y1, x2, y2):
#     return ((x2 + x1)**2 - (y2 + y1)**2) ** 0.25

def distance(x1, y1, x2, y2):
    # '''
    # Фунция вычисления расстояния между точками
    # >>> distance(0,0,3,4)
    # 5.0
    # >>> distance(0,0,0,0)
    # 0.0
    # '''
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


# python -m doctest -v .\pract5\1.py
# python -m doctest -v  .\pract5\first.doctest
