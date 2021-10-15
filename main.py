def calc(a, b, sign):
    if sign not in '+-/*':
        raise ValueError('Такой операции нет')
    if sign == '+':
        return a + b
    if sign == '-':
        return a - b
    if sign == '/':
        if b != 0:
            return round(a / b, 3)
        else:
            raise ValueError('На ноль делить нельзя')
    if sign == '*':
        return a * b
