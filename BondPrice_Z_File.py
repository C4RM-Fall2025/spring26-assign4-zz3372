
def getBondPrice_Z(face, couponRate, times, yc):

    price = 0
    coupon = face * couponRate
    
    for t, y in zip(times, yc):
        
        if t < times[-1]:
            cf = coupon
        else:
            cf = coupon + face
            
        price += cf / (1 + y) ** t
        
    return (price)
