from .foo import pow, add


def main():
    num = pow(2, 3)
    print(f"2 ^ 3 = {num}")
    num = add(2, 3)
    print(f"2 + 3 = {num}")


if __name__ == "__main__":
    main()
