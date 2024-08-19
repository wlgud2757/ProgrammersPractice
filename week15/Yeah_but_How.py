def main():
    S = input().strip()
    T = S.replace('()', '(1)')
    T = T.replace(')(', ')+(')
    print(T)

if __name__ == '__main__':
    main()
