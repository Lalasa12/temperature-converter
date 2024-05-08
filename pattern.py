def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)

def main():
    n = int(input("Enter a number: "))
    print("Sum of integers from 0 to", n, "is:", f(n))

if __name__ == "__main__":
    main()
