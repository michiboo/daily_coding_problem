def run_length_encode(text):
    count = 0
    cur = text[0]
    res = ''
    for x in text:
        if cur != x:
            res = res + str(count) + cur 
            cur = x
            count = 1
        else:
            count += 1
    res = res + str(count) + cur 
    print(res)
    return res

def run_length_decode(text):
    res = ''
    for x in range(0,len(text)-1,2):
        res = res + text[x+1] * int(text[x])
    return res


assert run_length_encode('AAAABBBCCDAA') == "4A3B2C1D2A"
assert run_length_decode('4A3B2C1D2A') == ('AAAABBBCCDAA')