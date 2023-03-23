from itertools import groupby


def rle_encode(s: str):

    return [(symb[0], len(symb)) for symb in [''.join(g) for _, g in groupby(s)]]


print(rle_encode('ABBCCCDEF'))
