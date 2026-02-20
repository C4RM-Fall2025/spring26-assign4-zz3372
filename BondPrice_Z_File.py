def getBondPrice_Z(face, couponRate, times, yc):

    c = face * couponRate
    price = 0
    n = len(times)

    for i, (t, y) in enumerate(zip(times, yc), start=1):
        cf = c
        if i == n:
            cf += face
        price += cf / (1 + y) ** t

    return price
