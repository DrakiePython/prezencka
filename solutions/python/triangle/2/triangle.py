def triangle_conf(sides:tuple[float, float, float])->bool:
    a, b, c = sorted(sides)
    return (a + b >= c) and (b + c >= a) and (a + c >= b) and a != 0 and b != 0 and c != 0

def equilateral(sides:tuple[float, float, float])->bool:
    a, b, c = sorted(sides)
    return triangle_conf(sides) and (a == b == c)


def isosceles(sides:tuple[float, float, float])->bool:
    a, b, c = sorted(sides)
    return triangle_conf(sides) and (a == b or a == c or b == c)


def scalene(sides:tuple[float, float, float])->bool:
    a, b, c = sorted(sides)
    return triangle_conf(sides) and (a != b and b != c and a != c) #{or} not isosceles(sides)  

