def itoBase(nb, base):
    le = len(base)
    result = ''
    while nb>0:
        result = base[nb%le] + result
        nb //= le
    print(result)

itoBase(168, '01')