

def main():

    assert (power(10, -2)) == 0.010000000000000002, "power(10, -2) failed"
    assert (power(10, -1)) == 0.1, "power(10, -1) failed"
    assert (power(10, 0)) == 1, "power(10, 0) failed"
    assert (power(10, 1)) == 10, "power(10, 1) failed"
    assert (power(10, 4)) == 10000, "power(10, 4) failed"
    print("PASSED")


def power(base, exp):

    if exp == 0:
        return 1
    
    elif exp < 0:
        return 1 / base * power(base, exp + 1)
    
    return base * power(base, exp - 1)



if __name__ == "__main__":
    main()