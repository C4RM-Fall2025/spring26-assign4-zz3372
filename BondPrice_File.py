def getBondPrice(y, face, couponRate, m, ppy=1):
    if ppy == 0:
        return face / (1 + y) ** m

    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    pvcoupons = c * (1 - (1 + r) ** (-n)) / r
    pvface = face * (1 + r) ** (-n)

    return (pvcoupons + pvface)
