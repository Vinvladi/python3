def main():
    with open('input.txt') as f:
        nums = f.read().split()

    a, b = map(int, nums)
    c = a + b

    with open('output.txt', 'w') as f:
        f.write(str(c))


if __name__ == '__main__':
    main()