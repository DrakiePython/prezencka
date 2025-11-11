def equilateral(sides:tuple[float, float, float])->bool:
    a, b, c = sorted(sides)
    decide = None
    if a <= 0 or b <= 0 or c <= 0:    # if any zero -> no triangle
        decide = False
    elif a == b == c:                 # if all sides equal = triangle is equilateral
        decide = True
    elif a != b or a != c:            # if any side is unequal = triangle is not equilateral
        decide = False
    return decide


def isosceles(sides:tuple[float, float, float])->bool:
    a, b, c = sorted(sides)
    decide = None
    if a <= 0 or b <= 0 or c <= 0:    # if any zero -> no triangle
        decide = False
    if a + b <= c:                    # checking inequality
        decide = False
    elif a == b or b == c:            # at least two sides are equal -> isosceles
        decide = True
    else:                             # geometrically, any other option mean triangle is scalene
        decide = False
    return decide


def scalene(sides:tuple[float, float, float])->bool:
    a, b, c = sorted(sides)
    decide = None
    if a == 0 or b == 0 or c == 0:     # if any zero -> no triangle
        decide = False
    elif a + b <= c:                   # checking inequality
        decide = False
    elif a != b and b != c and a != c: # all inequal -> scalene
        decide = True
    else:
        decide = False
    return decide

