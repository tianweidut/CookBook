#coding: utf-8
import string

alphabet = string.digits + string.ascii_letters 


def int_to_base62(number):
    r = []
    def div(n):
        r.append(alphabet[n % 62])
        if n >= 62:
            div(n / 62)
    
    div(number)
    return "".join(r[::-1])
    

def base62_to_int(b62):
    number = 0
    for order, val in enumerate(reversed(b62)):
        number +=  alphabet.index(val) * (62 ** order)
    return number

if __name__ == "__main__":
    for number in (253, 352, 52, 2, 11889743, 888888888888):
        b62 = int_to_base62(number)
        bnumber = base62_to_int(b62)
        print number, b62, bnumber, number == bnumber
