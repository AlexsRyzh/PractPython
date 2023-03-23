
def ham_dist(n1: int, n2: int):
    return sum([(n1 >> i) & 1 != (n2 >> i) & 1 for i in range(len(bin(max(n1, n2))[2:]))])


print(ham_dist(0b1100, 0b0011))
