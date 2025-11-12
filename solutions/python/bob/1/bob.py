def response(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob:
        response = 'Fine. Be that way!' 
    elif hey_bob.endswith('?') and hey_bob.isupper():
        response = 'Calm down, I know what I\'m doing!'
    elif hey_bob.isupper():
        response = 'Whoa, chill out!'
    elif hey_bob.endswith('?'):
        response = "Sure."
    else:
        response = 'Whatever.'
    return response
