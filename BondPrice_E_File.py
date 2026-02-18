def getBondPrice_E(face, couponRate, yc):
    price = 0
    coupon = face * couponRate
    for t, y in enumerate(yc, start=1):
        if t < len(yc):
            cf = coupon
        else:
            cf = coupon + face
        price += cf / (1 + y) ** t
    return (price)
