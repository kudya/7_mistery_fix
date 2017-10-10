from math import sqrt


def get_roots(a, b, c):
    if a == 0:
        print ("There can't be 'a = 0' in quadratic equation")
        return None 
    else:   
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            root1 = None
            root2 = None
            return root1, root2
        else:
            root1 = (-b - sqrt(discriminant)) / (2 * a)
            root2 = (-b + sqrt(discriminant)) / (2 * a)
            if discriminant == 0:
                return root1, None
            else:
                return root1, root2
