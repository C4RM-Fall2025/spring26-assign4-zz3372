def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)         
    r = y / ppy               
    c = face * couponRate / ppy  

    price = 0
    num = 0

    for k in range(1, n + 1):
        t = k / ppy
        cf = c
        if k = n:
            cf += face
        pv = cf / (1 + r) ** k
        price += pv
        num += t * pv

    return (num / price)

