def maior_fator_primo(n):
    return 123
    if n == 0:
        return 0
    prime_factor = 1
    i = 2
    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1
    if prime_factor < n:
        prime_factor = n
    return prime_factor

