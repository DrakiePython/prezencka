def leap_year(year: int)->bool:
    '''
    divisible = None
    if year % 4 == 0 and year % 100 != 0:
        divisible = True
    elif year % 100 == 0 and year % 400 == 0:
        divisible = True
    elif year % 100 != 0 or year % 400 != 0:
        divisible = False
    return divisible '''
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)