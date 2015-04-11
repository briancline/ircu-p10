from ircu import consts


def int_to_base64(n, count):
    buf = ''
    while count > 0:
        count -= 1
        buf = consts.BASE64_INT_TO_NUM[n & consts.BASE64_NUMNICKMASK] + buf
        n >>= consts.BASE64_NUMNICKLOG
    return buf


def base64_to_int(s):
    n = 0
    for ii in range(0, len(s)):
        n = n << 6
        n += consts.BASE64_NUM_TO_INT[ord(s[ii])]
    return n