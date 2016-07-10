import six

from ircu import consts


class Numeric(object):
    _length = consts.BASE64_SERVLEN

    def __init__(self, numeric):
        self._numeric = None
        self._numeric_str = None

        if isinstance(numeric, int):
            if numeric < 0:
                raise ValueError('Integer numerics cannot be negative')

            self._numeric = numeric
            self._numeric_str = int_to_base64(numeric, self._length)
        elif isinstance(numeric, six.string_types):
            self._numeric = base64_to_int(numeric)
            self._numeric_str = numeric
        else:
            raise TypeError('Numerics must be a string or integer type')

        if len(self._numeric_str) != self._length:
            raise ValueError('Numeric must be exactly %d characters' %
                             self._length)

    @property
    def int(self):
        return self._numeric

    def __str__(self):
        return self._numeric_str


class UserNumeric(Numeric):
    _length = consts.BASE64_USERLEN

    def __init__(self, numeric):
        super(UserNumeric, self).__init__(numeric)


class FullNumeric(Numeric):
    _length = consts.BASE64_SERVLEN + consts.BASE64_USERLEN

    def __init__(self, numeric):
        super(FullNumeric, self).__init__(numeric)
        self.server = Numeric(self._numeric_str[0:consts.BASE64_SERVLEN])
        self.user = UserNumeric(
            self._numeric_str[consts.BASE64_SERVLEN:self._length])


def int_to_base64(n, count):
    buf = ''
    while count:
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


def server_num_str(s):
    return int_to_base64(s, consts.BASE64_SERVLEN)


def user_num_str(s):
    return int_to_base64(s, consts.BASE64_USERLEN)


def server_num_int(s):
    return base64_to_int(s)


def user_num_int(s):
    return base64_to_int(s)
