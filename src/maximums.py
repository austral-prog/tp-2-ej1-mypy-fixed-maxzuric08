def max_of_two(x: int, y: int) -> int:
    if x >= y:
        return x
    elif x <= y:
        return y


def max_of_three(x: int, y: int, z: int) -> int:
    if y <= z and x <= z:
        return z
    elif z <= x and y <= x:
        return x
    elif x <= y and z <= y:
        return y
