def is_leap_year() -> bool:
    a:int = int(input('Ingrese un año: '))
    if (a%4 == 0 and a%100 == 0 and a%400 != 0) or (a%4 != 0):
        print('El año',a,'no es bisiesto')
        return False
    else:
        print('El año',a,'es bisiesto')
        return True
