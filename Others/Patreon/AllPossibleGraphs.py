MOD  = 10**9 + 7
def countGraphs(n):
    m = (n * (n-1)) // 2
    return pow(2, m, MOD)


if __name__ == "__main__":
    print(countGraphs(4))
    