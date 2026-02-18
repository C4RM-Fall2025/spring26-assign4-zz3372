

def getBondPrice(y, face, couponRate, m, ppy=1):
     y = y / ppy
    coupon = face * couponRate / ppy
    n = m * ppy
    
    x = 0
    
    for t in range(1, n + 1):
        x += coupon / (1 + y) ** t
        
    x += face / (1 + y) ** n
    return(x)
