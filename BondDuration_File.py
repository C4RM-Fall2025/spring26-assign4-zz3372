
def getBondDuration(y, face, couponRate, m, ppy=1):

    y = y / ppy
    coupon = face * couponRate / ppy
    n = m * ppy
    
    price = getBondPrice(y * ppy, face, couponRate, m, ppy)
    
    duration = 0
    
    for t in range(1, n + 1):
        cf = coupon
        if t == n:
            cf += face
            
        duration += t * cf / (1 + y) ** t
        
    duration = duration / price
    duration = duration / ppy
    
    return (duration)

