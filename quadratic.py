# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
   raiz = b**2 - 4*a*c
   if raiz > 0:
       raiz_resuelta =  raiz ** (1/2)
       r1 = (-b + raiz_resuelta) / (2 * a)
       r2 = (-b - raiz_resuelta) / (2 * a)
       return f"({r1}, {r2})"
   elif raiz == 0:
       r1 = (-b) / (2 * a)
       return f'({r1})'
   else:
       return "( )"




def value_y(a, b, c, x):
    a= a*(x**2)
    b= b*x
    r3 = a + b + c
    return r3

def to_string(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return "None"
    elif a == 0 :
        if b == 0:
            return f'f(x) = {c}'
        elif c == 0:
            return f'f(x) =  {b} * X'
        else:
            return f'f(x) = {b} * X + {c}'
    elif b == 0 :
        if a == 0:
            return f'f(x) = {c}'
        elif c == 0:
            return f'f(x) = {a} * X^2'
        else:
            return f'f(x) = {a} * X^2 + {c}'
    elif c == 0:
        if a == 0:
            return f'f(x) =  {b} * X'
        elif b == 0:
            return f'f(x) = {a} * X^2'
        else:
            return f'f(x) = {a} * X^2 + {b} * X'
    else:
        return f'f(x) = {a} * X^2 + {b} * X + {c}'



def derivation(a, b, c):
    if a == 0:
        if b == 0:
            return "f'(x) = 0"
        else:
            return f"f'(x) = {b}"
    elif b == 0:
        if a == c:
            return "f'(x) = 0"
        else:
            return f"f'(x) = {2 * a} * X"
    elif c == 0:
        if a == 0:
            return f"f'(x) = {b}"
        else:
            return f"f'(x) = {2 * a} * X"
    else:
        return f"f'(x) = {2 * a} * X + {b}"
