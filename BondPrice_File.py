

def getBondPrice(y, face, couponRate, m, ppy=1):

    pvcsum = 0
    n = int(m * ppy)
    coupon = face * couponRate / ppy
    rate = y / ppy

    for i in range(1, n + 1):
        pvcsum += coupon / (1 + rate) ** i

    pvcsum += face / (1 + rate) ** n

    return pvcsum

