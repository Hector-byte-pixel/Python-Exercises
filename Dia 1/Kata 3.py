def function(n: str):
    n = str(n)

    if int(n) == sum([
        p ** t
        for p, t in zip(
            [int(i) for i in n],
            range(1, len(n) + 1)
        )
    ]):
        return n


def sum_dig_pow(a, b):
    return [
        int(p)
        for p in [function(i) for i in range(a, b + 1)]
        if p != None
    ]