def getBondPrice_E(face, couponRate, yc):
    
    c = face * couponRate
    price = 0
    n = len(yc)
    
    for t, y in enumerate(yc, start=1):
        cf = c if t < n else (c + face)
        pv = 1 / (1 + y) ** t
        price += cf * pv

    return (price)
