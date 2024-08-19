import math

def main():
    K, P, N = map(int, input().split())

    MOD = 1000000007
    remainder = K * pow(P, N, MOD) % MOD
    print(remainder)

if __name__ == '__main__':
    main()
