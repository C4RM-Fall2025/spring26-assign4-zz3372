from decimal import Decimal, getcontext

getcontext().prec = 50  # high precision to make rounding stable

def getBondPrice(y, face, couponRate, m, ppy=1):
    y = Decimal(str(y))
    face = Decimal(str(face))
    couponRate = Decimal(str(couponRate))
    m = Decimal(str(m))
    ppy = int(ppy)

    if ppy == 0:  # zero-coupon (optional)
        return float(face / (Decimal(1) + y) ** int(m))

    n = int(m * ppy)                  # total periods
    r = y / Decimal(ppy)              # per-period yield
    c = face * couponRate / Decimal(ppy)  # per-period coupon

    one = Decimal(1)
    pv = Decimal(0)

    for t in range(1, n + 1):
        pv += c / (one + r) ** t
    pv += face / (one + r) ** n

    return float(pv)
