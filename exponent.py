def exponential(base, power):

    result = base

    if power == 0:
        result = 1
    else:
        for i in range(int(power) - 1):
            result = result * base

    return result
