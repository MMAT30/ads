
def main():

    assert (sumOfDigits(-12345)) == None, "sumOfDigits(-12345) failed"
    assert (sumOfDigits(-1)) == None, "sumOfDigits(-1) failed"
    assert (sumOfDigits(0)) == 0, "sumOfDigits(0) failed"
    assert (sumOfDigits(1)) == 1, "sumOfDigits(1) failed"
    assert (sumOfDigits(12345)) == 15, "sumOfDigits(12345) failed"
    print("PASSED")


def sumOfDigits(num: int):

    
    if num < 0:
        return None
    elif num == 0:
        return 0

    return (num % 10) + sumOfDigits( num // 10)


if __name__ == "__main__":
    main()