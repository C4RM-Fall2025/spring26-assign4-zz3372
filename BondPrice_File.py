

def getBondPrice(y, face, couponRate, m, ppy=1):
   pvcsum = 0

    for i in range(1, m * ppy + 1):

        cf = face * couponRate / ppy
        pvm = (1 + y / ppy) ** (-i)
        pvcf = pvm * cf
        pvcsum = pvcf + pvcsum

        if i = m * ppy:
            pvcsum = pvcsum + face * pvm

    return(pvcsum)
