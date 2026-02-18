def getBondPrice(y, face, couponRate, m, ppy=1):

    pvcsum = 0
    n = m * ppy
    coupon = face * couponRate / ppy
    t = y / ppy

    for i in range(1, n + 1):
        pvcsum += coupon / (1 +t) ** i

    pvcsum += face / (1 + t) ** n

    return （pvcsum）

