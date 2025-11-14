def is_armstrong_number(number:int)->bool:
    # transforming integer into string
    number_str = str(number)
    # counting the length of number
    n = len(number_str)
    # map applies lamda d: int(d), which converts each string back into integer, into each string 
    # list puts results into a list of digits
    digits = list(map(lambda dig: int(dig), str(number)))
    # lambda dig: dig**n raises each digit to the power of n, map applies it to all digits and sum adds them together
    result = sum(map(lambda dig: dig ** n, digits))
    return result == number