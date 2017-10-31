import math
def modexp_lr(a, b, n):
    r = 1
    for bit in reversed(_bits_of_n(b)):
        r = r * r % n
        if bit == 1:
            r = r * a % n
    return r

def _bits_of_n(n):
    bits = []
    while n:
        bits.append(n % 2)
        n /= 2
    return bits

def p_factors(num, num_c, p_to_test, prime_factors):
    while num_c % 2 == 0:
        num_c /= 2
        if 2 in prime_factors:
            prime_factors[2] += 1
        else:
            prime_factors[2] = 1
    for x in xrange(3, int(math.sqrt(num_c))+1,2):
        while num_c % x == 0:
            if x in prime_factors:
                prime_factors[x] += 1
            else:
                prime_factors[x] = 1
            num_c /= x
    if num_c > 2:
        prime_factors[num_c] = 1
    p_to_test = [(num-1)/x for x in prime_factors]
    return p_to_test, prime_factors

def main():
    num = input()
    num_c = num-1
    p_to_test = []
    prime_factors = {}
    p_to_test,prime_factors = p_factors(num, num_c, p_to_test, prime_factors)
    num_of_p_roots = 1
    for key,value in prime_factors.iteritems():
        num_of_p_roots *= (((key ** value)/key) * ((key-1)))
            
    for x in xrange(2, num):
        flag = 0
        for y in p_to_test:
            if modexp_lr(x,y,num) != 1:
                flag += 1
        if flag == len(p_to_test):
            print x, num_of_p_roots
            break

main()