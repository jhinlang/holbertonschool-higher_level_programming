def add_integer(a, b=98):
    try:
        a = int(a)
        b = int(b)
        result = a + b
    except TypeError:
        print("a doit être un entier ou b doit être un entier")
    finally
        return result
